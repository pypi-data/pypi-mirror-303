import copy
import json
from datetime import datetime
from typing import Any, Dict, List, Tuple, Union
from typing import Optional

from perun.connector import AdaptersManager
from perun.connector import Logger
from perun.connector.adapters.AdaptersManager import AdaptersManagerNotExistsException
from sqlalchemy import MetaData, delete, select, update
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session

from perun.proxygui import jwt
from perun.proxygui.jwt import SingletonJWTServiceProvider
from perun.utils.ConfigStore import ConfigStore
from perun.utils.CustomExceptions import UserNotExistsException
from perun.utils.DatabaseService import DatabaseService
from perun.utils.EmailService import EmailService
from perun.utils.Notification import NotificationType


class UserManager:
    def __init__(self, cfg):
        USER_MANAGER_CFG = cfg.get("user_manager", {})
        GLOBAL_CONFIG = ConfigStore.get_global_cfg(
            USER_MANAGER_CFG.get("global_cfg_filepath")
        )
        ADAPTERS_MANAGER_CFG = GLOBAL_CONFIG["adapters_manager"]
        ATTRS_MAP = ConfigStore.get_attributes_map(GLOBAL_CONFIG["attrs_cfg_path"])
        self.USER_NOT_EXISTS_EXCEPTION_NAME = "UserNotExistsException"

        self._ADAPTERS_MANAGER = AdaptersManager(ADAPTERS_MANAGER_CFG, ATTRS_MAP)
        self._SUBJECT_ATTRIBUTE = USER_MANAGER_CFG.get(
            "perun_person_principal_names_attribute"
        )
        self._KEY_ID = USER_MANAGER_CFG["key_id"]
        self._KEYSTORE = USER_MANAGER_CFG["keystore"]

        if isinstance(cfg.get("heuristic_page", None), dict):
            self._NAME_ATTRIBUTE = cfg.get("heuristic_page", {}).get(
                "perun_user_name_attribute"
            )

        if isinstance(cfg.get("mfa_reset", None), dict):
            self.email_service = EmailService(cfg)
            self._PREFERRED_MAIL_ATTRIBUTE = cfg.get("mfa_reset", {}).get(
                "preferred_mail_attribute"
            )
            self._ALL_MAILS_ATTRIBUTE = cfg.get("mfa_reset", {}).get(
                "all_mails_attribute"
            )

        self.database_service = DatabaseService(cfg)
        self.jwt_service = SingletonJWTServiceProvider.get_provider().get_service()

        self.logger = Logger.get_logger(__name__)
        self._cfg = USER_MANAGER_CFG

    def extract_user_attribute_single(self, attr_name: str, user_id: int) -> Any:
        attr_value = self.extract_user_attribute(attr_name, user_id)
        if attr_value and isinstance(attr_value, list):
            return attr_value[0]

        return attr_value

    def extract_user_attribute(self, attr_name: str, user_id: int) -> Any:
        try:
            user_attrs = self._ADAPTERS_MANAGER.get_user_attributes(
                user_id, [attr_name]
            )
            return user_attrs.get(attr_name)
        except AdaptersManagerNotExistsException as e:
            # Wrap an exception to deal with it in the GUI
            if self.USER_NOT_EXISTS_EXCEPTION_NAME in e.message:
                raise UserNotExistsException(e.message)

            raise e

    def _revoke_ssp_sessions(
        self,
        subject: str = None,
        session_id: str = None,
    ) -> int:
        ssp_engine = self.database_service.get_postgres_engine("ssp_database")
        sessions_table_name = self._cfg["ssp_database"]["sessions_table_name"]
        ssp_sessions_table = self.database_service.get_postgres_table(
            ssp_engine, sessions_table_name
        )

        with ssp_engine.begin() as conn:
            if session_id:
                delete_query = ssp_sessions_table.delete().where(
                    (ssp_sessions_table.c._type == "session")
                    & (ssp_sessions_table.c._key == session_id)
                )
            elif subject:
                delete_query = ssp_sessions_table.delete().where(
                    ssp_sessions_table.c.eduperson_principal_name == subject
                )
            else:
                self.logger.error(
                    "Unknown subject and session_id, cannot remove SSP session"
                )
                return 0
            result = conn.execute(delete_query)
            deleted_count = result.rowcount
        return deleted_count

    def _remove_ssp_session_index(self, ssp_session_id: str, client_id: str) -> None:
        """Removes single RP session index from SimpleSAMLSession"""

        entry = self._get_ssp_session_by_key(ssp_session_id)
        if not entry:
            self.logger.debug(
                "No session found for %s, cannot remove index.", ssp_session_id
            )
            return
        session_details = entry.get("session_indexes_detail", {})
        session_indexes = entry.get("session_indexes", [])
        original_count = len(session_indexes)
        for issuer, data in session_details.items():
            for sp, sid in data.items():
                if sp == client_id:
                    del data[sp]
                    session_indexes.remove(sid)
                    break
        if session_indexes and len(session_indexes) != original_count:
            self.logger.info(
                f"Removed single session index for client_id {client_id} in session "
                f"{ssp_session_id}"
            )
            self._update_ssp_session_indexes(
                ssp_session_id, entry.get("_expire"), session_indexes, session_details
            )

    def _get_mitre_delete_statements(
        self,
        engine: Engine,
        user_id: str = None,
        session_id: str = None,
        include_refresh_tokens=False,
    ) -> list[Any]:
        meta_data = MetaData()
        meta_data.reflect(engine)
        session = Session(bind=engine)

        # tables holding general auth data
        AUTH_HOLDER_TBL = meta_data.tables["authentication_holder"]
        SAVED_USER_AUTH_TBL = meta_data.tables["saved_user_auth"]

        matching_username = SAVED_USER_AUTH_TBL.c.name == user_id
        if session_id:
            # if session id is present, we only delete tokens associated with a
            # single specified session
            session_id_attr = (
                self._cfg["mitre_database"]["ssp_session_id_attribute"]
                or "urn:cesnet:proxyidp:attribute:sspSessionID"
            )
            matching_sid = SAVED_USER_AUTH_TBL.c.authentication_attributes.like(
                f'%"{session_id_attr}":["{session_id}"]%'
            )
            user_auth = session.query(SAVED_USER_AUTH_TBL.c.id).filter(
                matching_sid & matching_username
            )
        elif user_id:
            # if only user id is present, we delete all tokens associated
            # with the user
            user_auth = session.query(SAVED_USER_AUTH_TBL.c.id).filter(
                matching_username
            )
        else:
            return []

        # tables holding tokens
        ACCESS_TOKEN_TBL = meta_data.tables["access_token"]
        AUTH_CODE_TBL = meta_data.tables["authorization_code"]
        DEVICE_CODE = meta_data.tables["device_code"]

        token_tables = [ACCESS_TOKEN_TBL, AUTH_CODE_TBL, DEVICE_CODE]

        if include_refresh_tokens:
            REFRESH_TOKEN_TBL = meta_data.tables["refresh_token"]
            token_tables.append(REFRESH_TOKEN_TBL)

        delete_statements = []
        for token_table in token_tables:
            delete_statements.append(
                delete(token_table).where(
                    token_table.c.auth_holder_id.in_(
                        session.query(AUTH_HOLDER_TBL.c.id).filter(
                            AUTH_HOLDER_TBL.c.user_auth_id.in_(user_auth)
                        )
                    )
                )
            )

        return delete_statements

    def _delete_mitre_tokens(
        self,
        user_id: str = None,
        session_id: str = None,
        include_refresh_tokens: bool = False,
    ) -> int:
        deleted_mitre_tokens_count = 0

        engine = self.database_service.get_postgres_engine("mitre_database")
        statements = self._get_mitre_delete_statements(
            engine, user_id, session_id, include_refresh_tokens
        )
        with engine.begin() as cnxn:
            for stmt in statements:
                result = cnxn.execute(stmt)
                deleted_mitre_tokens_count += result.rowcount

        return deleted_mitre_tokens_count

    def sub_to_user_id(self, sub: str, issuer: str) -> Optional[str]:
        """
        Get Perun user ID using user's 'sub' attribute
        :param sub: Perun user's subject attribute
        :return: Perun user ID
        """
        if sub and issuer:
            user = self._ADAPTERS_MANAGER.get_perun_user(idp_id=issuer, uids=[sub])
            if user:
                return str(user.id)

    def logout(
        self,
        user_id: str = None,
        session_id: str = None,
        include_refresh_tokens: bool = False,
    ) -> None:
        """
        Performs revocation of user's sessions based on the provided user_id or
        session_id. If none are provided, revocation is not performed. If
        both are
        provided, only a single session is revoked if it exists. If only
        user id is
        provided, all of user's sessions are revoked.
        :param user_id: id of user whose sessions are to be revoked
        :param session_id: id of a specific session to revoke
        :param include_refresh_tokens: specifies whether refresh tokens
        should be
        canceled as well
        :return: Nothing
        """
        if not user_id:
            self.logger.info(
                "No user id provided. Please, provide at least user id to "
                "perform "
                "logout."
            )
            return
        subject = self.extract_user_attribute_single(
            self._SUBJECT_ATTRIBUTE, int(user_id)
        )

        deleted_tokens_count = self._delete_mitre_tokens(
            user_id=user_id, include_refresh_tokens=include_refresh_tokens
        )

        revoked_sessions_count = self._revoke_ssp_sessions(subject, session_id)

        self.logger.info(
            f"Logged out user {subject} from {revoked_sessions_count} SSP sessions,"
            f"deleted {deleted_tokens_count} mitre tokens."
        )

    def logout_from_service_op(self, subject, ssp_session_id, client_id) -> None:
        self._remove_ssp_session_index(ssp_session_id, client_id)
        # todo - keep skipping mitre?

    def get_active_client_ids_for_user(self, sub: str) -> set[str]:
        """
        Returns list of unique client ids retrieved from active user's
        sessions.
        :param sub: user, whose sessions are retrieved
        :return: list of client ids
        """
        # todo -- when user_id is stored in SSP db, this conversion will be needed
        # subject = self.extract_user_attribute_single(self._SUBJECT_ATTRIBUTE, int(sub))

        ssp_clients = self._get_ssp_entity_ids_by_user(sub)
        mitre_clients = self._get_mitre_client_ids_by_attribute(user_id=sub)

        return ssp_clients + mitre_clients

    def get_active_client_ids_for_session(self, session_id: str):
        ssp_clients = self._get_ssp_entity_ids_by_session(session_id)
        mitre_clients = self._get_mitre_client_ids_by_attribute(session_id=session_id)

        return ssp_clients + mitre_clients

    def _get_mitre_client_ids_by_attribute(self, session_id=None, user_id=None):
        engine = self.database_service.get_postgres_engine("mitre_database")
        meta_data = MetaData()
        meta_data.reflect(engine)
        session = Session(bind=engine)

        AUTH_HOLDER_TBL = meta_data.tables["authentication_holder"]
        SAVED_USER_AUTH_TBL = meta_data.tables["saved_user_auth"]
        ACCESS_TOKEN_TBL = meta_data.tables["access_token"]
        CLIENT_DETAILS_TBL = meta_data.tables["client_details"]

        session_id_attr = (
            self._cfg["mitre_database"]["ssp_session_id_attribute"]
            or "urn:cesnet:proxyidp:attribute:sspSessionID"
        )

        # Not clear according witch attribute to search
        if (session_id is None) == (user_id is None):
            return []

        matching_attr = False
        # Search by session id
        if session_id is not None:
            matching_attr = SAVED_USER_AUTH_TBL.c.authentication_attributes.like(
                f'%"{session_id_attr}":["{session_id}"]%'
            )

        # Search by user id
        if user_id is not None:
            matching_attr = SAVED_USER_AUTH_TBL.c.name == user_id

        with engine.begin() as cnxn:
            # Get pair of user_id and session_id based on input attribute
            stmt = select(
                SAVED_USER_AUTH_TBL.c.id,
                SAVED_USER_AUTH_TBL.c.authentication_attributes,
            ).where(matching_attr)
            result = cnxn.execute(stmt)
            result_dict = [
                r for r in result
            ]  # [(id, attrs(for session_id retrieval)))]

            uid_sid_dict = []
            # Retrieve right format of session id from auth attrs
            for uid, auth_attrs in result_dict:
                sid = json.loads(auth_attrs).get(session_id_attr)
                uid_sid_dict.append((uid, sid))

            uid_sid_dict = list(set(uid_sid_dict))

            combined_result_dict = []

            # Retrieve token value based on each user_ids
            # -------------------------------------------
            for uid, sid in uid_sid_dict:
                stmt = select(
                    ACCESS_TOKEN_TBL.c.client_id, ACCESS_TOKEN_TBL.c.token_value
                ).where(
                    ACCESS_TOKEN_TBL.c.auth_holder_id.in_(
                        session.query(AUTH_HOLDER_TBL.c.id).filter(
                            AUTH_HOLDER_TBL.c.user_auth_id == uid
                        )
                    )
                )
                result = cnxn.execute(stmt)
                result_dict = [r for r in result]  # [(token_client_id, token_value)]

                # Retrieve client_id for each token_client_id
                # -------------------------------------------
                for token_client_id, token_value in result_dict:
                    # Get issuer from token_value
                    issuer = self._get_issuer_from_id_token(token_value)

                    # Another select for clients_ids
                    stmt = select(CLIENT_DETAILS_TBL.c.client_id).where(
                        CLIENT_DETAILS_TBL.c.id == token_client_id
                    )
                    result = cnxn.execute(stmt)
                    client_ids = [r[0] for r in result]

                    for client_id in client_ids:
                        combined_result_dict.append((client_id, sid, issuer, None))

        return list(set(combined_result_dict))

    def get_user_id_by_ssp_session_id(self, ssp_session_id: str) -> Union[str, None]:
        if ssp_session_id is None:
            return None
        entry = self._get_ssp_session_by_key(ssp_session_id)
        return entry.get("eduperson_principal_name") if entry is not None else None

    def _get_ssp_session_by_key(self, ssp_session_id) -> Union[Dict[str, Any], None]:
        """
        Returns SSP session by its key (SimpleSAMLSessionID passed in cookies).
        Uses existing db indexes.
        :param ssp_session_id: SimpleSAMLSessionID
        :return: session as stored in db or None if not found
        """
        current_datetime = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        ssp_engine = self.database_service.get_postgres_engine("ssp_database")
        sessions_table_name = self._cfg["ssp_database"]["sessions_table_name"]
        ssp_sessions_table = self.database_service.get_postgres_table(
            ssp_engine, sessions_table_name
        )

        with ssp_engine.begin() as conn:
            query = select(ssp_sessions_table).where(
                (
                    (ssp_sessions_table.c._type == "session")
                    & (ssp_sessions_table.c._key == ssp_session_id)
                    & (
                        (ssp_sessions_table.c._expire > current_datetime)
                        | (ssp_sessions_table.c._expire is None)
                    )
                )
            )

            result = conn.execute(query)
            row = result.first()
            if row:
                row_dict = {
                    column_name: value for column_name, value in zip(result.keys(), row)
                }
                row_dict["session_indexes_detail"] = (
                    json.loads(row_dict["session_indexes_detail"])
                    if row_dict.get("session_indexes_detail")
                    else {}
                )
                return row_dict
            else:
                return None

    def _update_ssp_session_indexes(
        self, session_id, expiration, session_indexes, session_details
    ) -> None:
        """
        Updates SimpleSAMLSession's RP sessions
        :param session_id: the original session key
        :param expiration: the original expiration (so we could use index)
        :param session_indexes: new session indexes
        :param session_details: new session details
        """
        ssp_engine = self.database_service.get_postgres_engine("ssp_database")
        sessions_table_name = self._cfg["ssp_database"]["sessions_table_name"]
        ssp_sessions_table = self.database_service.get_postgres_table(
            ssp_engine, sessions_table_name
        )

        with ssp_engine.begin() as conn:
            update_query = (
                update(ssp_sessions_table)
                .where(
                    (
                        (ssp_sessions_table.c._type == "session")
                        & (ssp_sessions_table.c._key == session_id)
                        & (
                            (ssp_sessions_table.c._expire == expiration)
                            | (ssp_sessions_table.c._expire is None)
                        )
                    )
                )
                .values(
                    session_indexes_detail=json.dumps(session_details),
                    session_indexes=session_indexes,
                )
            )

            conn.execute(update_query)

    def _get_ssp_entity_ids_by_user(self, sub: str) -> List[Tuple[str, str, str]]:
        ssp_engine = self.database_service.get_postgres_engine("ssp_database")
        sessions_table_name = self._cfg["ssp_database"]["sessions_table_name"]
        ssp_sessions_table = self.database_service.get_postgres_table(
            ssp_engine, sessions_table_name
        )

        with ssp_engine.begin() as conn:
            sql_query = select(ssp_sessions_table.c.session_indexes_detail).where(
                ssp_sessions_table.c.eduperson_principal_name == sub
            )

            result = conn.execute(sql_query)

            entries = result.fetchall()
            result = []
            for entry in entries:
                session_details = json.loads(entry[0] or "{}")
                for issuer, data in session_details.items():
                    for sp, sid in data.items():
                        if "saml:NameID" in sid:
                            result.append(
                                (
                                    sp,
                                    sid["saml:SessionIndex"],
                                    issuer,
                                    sid["saml:NameID"],
                                )
                            )
                        else:
                            result.append((sp, sid, issuer, None))

        return result

    def _get_ssp_entity_ids_by_session(
        self, session_id: str
    ) -> List[Tuple[str, str, str]]:
        entry = self._get_ssp_session_by_key(session_id)

        result = []
        session_details = (
            entry.get("session_indexes_detail", {}) if entry is not None else {}
        )
        for issuer, data in session_details.items():
            for sp, sid in data.items():
                if "saml:NameID" in sid:
                    result.append(
                        (sp, sid["saml:SessionIndex"], issuer, sid["saml:NameID"])
                    )
                else:
                    result.append((sp, sid, issuer, None))
        return result

    def handle_mfa_reset(
        self,
        user_id: str,
        locale: str,
        notif_type: NotificationType,
    ) -> str:
        """
        For verification, sends link with reset URL to preferred mail and notifies
        other mail addresses about the reset.
        For confirmation, notifies all mail addresses the reset was performed.
        :return: preferred mail
        """
        preferred_mail = self.extract_user_attribute_single(
            self._PREFERRED_MAIL_ATTRIBUTE, int(user_id)
        )
        all_user_mails = None
        if self._ALL_MAILS_ATTRIBUTE:
            all_user_mails = self.extract_user_attribute(
                self._ALL_MAILS_ATTRIBUTE, int(user_id)
            )
        if notif_type == NotificationType.VERIFICATION:
            # send MFA reset confirmation link
            self.email_service.send_mfa_reset_link(user_id, preferred_mail, locale)

            # send notification about MFA reset
            if all_user_mails:
                non_preferred_mails = copy.deepcopy(all_user_mails)
                if preferred_mail in all_user_mails:
                    non_preferred_mails.remove(preferred_mail)
                if non_preferred_mails:
                    self.email_service.send_mfa_reset_notification(
                        non_preferred_mails, locale, notif_type
                    )

        elif notif_type == NotificationType.CONFIRMATION:
            self.email_service.send_mfa_reset_notification(
                all_user_mails, locale, notif_type
            )

        else:
            raise Exception("Unknown notification type: " + notif_type.name)

        return preferred_mail

    def forward_mfa_reset_request(
        self, requester_id: str, requester_email: str
    ) -> None:
        self.email_service.send_mfa_reset_request(requester_id, requester_email)

    def _get_issuer_from_id_token(self, id_token):
        claims = jwt.decode_jwt_without_verification(id_token)
        issuer = claims.get("iss")
        return issuer

    def get_all_rp_names(self):
        """
        Returns structure of {client_id: {'cs': cs_label, 'en': en_label}
        from Perun mfaCategories attribute
        """
        result = {}
        names = self._ADAPTERS_MANAGER.get_entityless_attribute(
            "urn:perun:entityless:attribute-def:def:mfaCategories"
        )
        if "categories" not in names:
            self.logger.warn(
                "Attribute containing services names not returned or format is invalid!"
            )
            return {}
        services_structure = json.loads(names["categories"])
        for category in services_structure:
            result = result | services_structure[category]["rps"]
        return result

    def get_user_name(self, user_id: int):
        name = ""
        if self._NAME_ATTRIBUTE:
            name = self.extract_user_attribute_single(self._NAME_ATTRIBUTE, user_id)

        return name
