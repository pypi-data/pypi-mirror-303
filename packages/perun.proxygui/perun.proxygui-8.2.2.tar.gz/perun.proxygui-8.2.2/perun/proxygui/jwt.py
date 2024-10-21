import base64
import json
import os
import secrets
from datetime import datetime, timedelta
from typing import Dict, Any

from cryptojwt import JWT
from cryptojwt.key_jar import init_key_jar
from perun.utils.ConfigStore import ConfigStore
from perun.utils.CustomExceptions import InvalidJWTError
from perun.utils.DatabaseService import DatabaseService
from perun.connector import Logger
from sqlalchemy import MetaData, select, insert

logger = Logger.get_logger(__name__)


class JWTService:
    def __init__(self, cfg, keystore, key_id):
        self.__KEYSTORE = keystore
        self.__KEY_ID = key_id
        self.__CFG = cfg

        if self.__KEYSTORE and os.path.exists(self.__KEYSTORE) and self.__KEY_ID:
            key_jar = init_key_jar(
                private_path=self.__KEYSTORE, issuer_id=self.__KEY_ID
            )
            self.__JWT = JWT(key_jar=key_jar, iss=self.__KEY_ID)

        self.__DATABASE_SERVICE = DatabaseService(self.__CFG)

    def verify_jwt(self, token) -> Dict[Any, Any]:
        """
        Verifies that the JWT is valid - it is not expired and hasn't been
        used yet.

        :param token: JWT to verify
        :return: content of the JWT if it's valid, raise InvalidJWTError otherwise
        """
        try:
            claims = self.__JWT.unpack(token)
        except Exception as e:
            raise InvalidJWTError(
                f"Unpacking of JWT failed because of an internal error: '{e}'"
            )

        # verify that the token is not expired
        expiration_date = datetime.fromtimestamp(claims.get("exp"))
        if datetime.now() >= expiration_date:
            raise InvalidJWTError(f"JWT has already expired on: {expiration_date}")

        # verify that the token hasn't been used yet
        nonce = claims.get("nonce")
        engine = self.__DATABASE_SERVICE.get_postgres_engine("jwt_nonce_database")

        with engine.begin() as cnxn:
            meta_data = MetaData()
            meta_data.reflect(engine)

            jwt_nonce_table = self.__DATABASE_SERVICE.get_postgres_table(
                engine, self.__CFG.get("jwt_nonce_database", {}).get("table_name")
            )

            query = select(jwt_nonce_table.c.used_nonce).where(
                jwt_nonce_table.c.used_nonce == nonce
            )
            result = cnxn.execute(query).fetchone()

            if result is not None:
                raise InvalidJWTError("JWT has nonce that has been used already")

            query = insert(jwt_nonce_table).values(used_nonce=nonce)
            cnxn.execute(query)

        return claims

    def get_jwt(
        self, token_args: Dict[str, Any] = None, lifetime_hours: int = 24
    ) -> str:
        """
        Constructs a signed JWT containing expiration time and nonce by
        default. Other attributes to be added can be passed in token_args.

        :param token_args: dict of attributes to be added to the signed JWT
        :param lifetime_hours: How long should the token stay valid
        :return: signed and encoded JWT
        """
        exp_time = datetime.utcnow() + timedelta(hours=lifetime_hours)
        token_info = {
            "nonce": secrets.token_urlsafe(16),
            "exp": exp_time.timestamp(),
        }

        if token_args:
            token_info.update(token_args)

        encoded_token = self.__JWT.pack(payload=token_info, kid=self.__KEY_ID)

        return encoded_token


class JWTServiceProvider:
    """
    Provides configured instances of JWTService for signing and verifying JWTs. The
    default service is configured without an issuer using key defined by <key_id>,
    located at <keystore> from proxygui config. Other JWTService instances are based
    on the <issuers> specified in proxygui config.
    """

    __jwt_services = {}
    __default_jwt_service = None

    @classmethod
    def is_initialized(cls):
        return cls.__jwt_services or cls.__default_jwt_service

    @classmethod
    def initialize(cls):
        cfg = ConfigStore.get_config()
        issuers_list = cfg.get("issuers")
        cls.__jwt_services = {}
        if issuers_list:
            cls.__jwt_services = {
                issuer.get("issuer"): JWTService(
                    cfg, issuer.get("keystore"), issuer["issuer"]
                )
                for issuer in issuers_list
            }
        cls.__default_jwt_service = JWTService(
            cfg, cfg.get("keystore"), cfg.get("key_id")
        )  # service without a specified issuer

    @classmethod
    def get_service(cls) -> JWTService:
        """
        Obtain a generic instance of JWTService when issuer is not known or needed.
        :return: JWTService
        """
        return cls.__default_jwt_service

    @classmethod
    def get_service_by_issuer(cls, issuer: str) -> JWTService:
        """
        Get JWTService configured for given issuer. In case the issuer does not exist
        in config, default instance without an issuer is returned
        :param issuer: JWTService
        :return:
        """
        return cls.__jwt_services.get(issuer, cls.__default_jwt_service)


def decode_jwt_without_verification(token):
    """Decodes payload of JWT token without validating it.

    :param token: token to be decoded
    :return: decoded payload
    """
    try:
        header, payload, signature = token.split(".")
        decoded_payload = base64.urlsafe_b64decode(payload + "==").decode("utf-8")
        return json.loads(decoded_payload)
    except Exception as e:
        raise InvalidJWTError(e)


class SingletonJWTServiceProvider:
    __provider = JWTServiceProvider()

    @classmethod
    def get_provider(cls) -> JWTServiceProvider:
        if not cls.__provider.is_initialized():
            cls.__provider.initialize()

        return cls.__provider
