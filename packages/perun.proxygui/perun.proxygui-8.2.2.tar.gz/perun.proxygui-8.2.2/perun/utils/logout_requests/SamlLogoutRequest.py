from perun.connector import Logger
from saml2.server import Server, BINDING_HTTP_REDIRECT
from perun.utils.logout_requests.LogoutRequest import LogoutRequest
from saml2.saml import NameID, NAMEID_FORMAT_UNSPECIFIED
from datetime import datetime, timedelta
import uuid


class SamlLogoutRequest(LogoutRequest):
    """Prepares SAML request. Currently supports only redirect binding
    (called in iframe directly), expecting callback to our endpoint."""

    def __init__(self, op_id, client_id, rp_names):
        LogoutRequest.__init__(self, op_id, client_id, rp_names, "SAML_LOGOUT")
        self.logger = self.logger = Logger.get_logger(__name__)
        self.sign_alg = "http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"

    def prepare_logout(self, cfg, name_id, sid=None):
        rp_config = (
            cfg.get("RPS", {})
            .get(self.client_id, {})
            .get("SAML_LOGOUT", {})
            .get(self.op_id)
        )

        location = rp_config["location"].get("location")
        if rp_config.get("binding") == BINDING_HTTP_REDIRECT:
            saml_request = self.prepare_saml_request(
                name_id, sid, location, rp_config["saml_idp_conf"]
            )
            for url in saml_request:
                if url[0] == "Location":
                    self.iframe_src = url[1]
                    # FIXME possible multiple urls with location - probably because of multiple sessions

    def prepare_saml_request(self, name_id, sid, location, idp_config) -> str:
        current_time = datetime.utcnow() + timedelta(minutes=5)
        formatted_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.msg_id = f"_{uuid.uuid4().hex + uuid.uuid4().hex[:10]}"

        idp = Server(idp_config)
        lreq_id, lreq = idp.create_logout_request(
            location,
            issuer_entity_id=self.op_id,
            name_id=NameID(
                text=name_id,
                format=NAMEID_FORMAT_UNSPECIFIED,
                sp_name_qualifier=self.client_id,
            ),
            session_indexes=[sid],
            sign=False,
            expire=formatted_time,
            message_id=self.msg_id,
        )
        lreq = idp.apply_binding(
            BINDING_HTTP_REDIRECT,
            msg_str=lreq,
            destination=location,
            sign=True,
            sigalg=self.sign_alg,
        )
        return lreq["headers"]
