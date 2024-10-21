from http import HTTPStatus

from authlib.integrations.flask_oauth2 import current_token
from flask import (
    request,
    jsonify,
    abort,
    session,
    redirect,
    Response,
)
from perun.connector import Logger
import flask_smorest as fs

from perun.proxygui.jwt import SingletonJWTServiceProvider
from perun.proxygui.oauth import require_oauth
from perun.proxygui.user_manager import UserManager
from perun.utils.CustomExceptions import InvalidJWTError
from perun.utils.consent_framework.consent import Consent
from perun.utils.consent_framework.consent_manager import (
    ConsentManager,
    InvalidConsentRequestError,
)
from perun.proxygui.openapi.openapi_data import openapi_route, apis_desc

logger = Logger.get_logger(__name__)


def construct_consent_api(cfg):
    consent_openapi_api = fs.Blueprint(
        "Consent API",
        __name__,
        url_prefix="/proxygui",
        description=apis_desc.get("consent", ""),
    )

    CONSENT_CFG = cfg.get("consent_api")

    db_manager = ConsentManager(CONSENT_CFG)
    user_manager = UserManager(CONSENT_CFG)
    jwt_service = SingletonJWTServiceProvider.get_provider().get_service()

    oauth_cfg = CONSENT_CFG["oidc_provider"]

    @openapi_route("/verify/<string:consent_id>", consent_openapi_api)
    def verify(consent_id):
        attrs = db_manager.fetch_consented_attributes(consent_id)
        if attrs:
            return jsonify(attrs)
        logger.debug("no consent found for id '%s'", consent_id)
        abort(401)

    @openapi_route("/creq/<string:jwt>", consent_openapi_api)
    def creq(jwt):
        if request.method == "POST":
            jwt = request.values.get("jwt")
        try:
            jwt = jwt_service.verify_jwt(jwt)
            ticket = db_manager.save_consent_request(jwt)
            return ticket
        except InvalidJWTError as e:
            logger.debug("JWT validation failed: %s, %s", str(e), jwt)
            abort(400)
        except InvalidConsentRequestError as e:
            logger.debug("received invalid consent request: %s, %s", str(e), jwt)
            abort(400)

    @openapi_route("/save_consent", consent_openapi_api)
    def save_consent():
        state = request.args["state"]
        validation = "validation" in request.args
        consent_status = request.args["consent_status"]
        requester = session["requester_name"]
        user_id = session["user_id"]
        redirect_uri = session["redirect_endpoint"]
        month = request.args["month"]

        attributes = request.args.to_dict()
        if "validation" in attributes:
            attributes.pop("validation")
        attributes.pop("consent_status")
        attributes.pop("state")
        attributes.pop("month")

        for attr in session["locked_attrs"]:
            attributes[attr] = session["attr"][attr]

        if state != session["state"]:
            abort(403)
        if consent_status == "yes" and not set(attributes).issubset(
            set(session["attr"])
        ):
            abort(400)

        if consent_status == "yes" and validation:
            consent = Consent(attributes, user_id, requester, int(month))
            db_manager.save_consent(session["id"], consent)
            session.clear()

        if consent_status == "no":
            return redirect(cfg["redirect_url"])
        return redirect(redirect_uri)

    # scopes in form ['scope1 scope2'] represent logical conjunction in Authlib
    required_scopes = [" ".join(oauth_cfg["scopes"])]

    @openapi_route("/users/me/consents", consent_openapi_api)
    @require_oauth(required_scopes)
    def consents():
        scopes = current_token.scopes
        sub = scopes.get("sub")
        issuer = CONSENT_CFG["oidc_provider"]["issuer"]
        user_id = user_manager.sub_to_user_id(sub, issuer)
        if not user_id:
            error_message = f"Could not fetch user ID for subject ID '{sub}'"
            return Response(error_message, HTTPStatus.INTERNAL_SERVER_ERROR)

        user_consents = db_manager.fetch_all_user_consents(user_id)

        return jsonify({"consents": user_consents})

    @openapi_route("/users/me/consents/<string:consent_id>", consent_openapi_api)
    @require_oauth(required_scopes)
    def delete_consent(consent_id):
        deleted_count = db_manager.delete_user_consent(consent_id)

        if deleted_count > 0:
            return jsonify(
                {
                    "deleted": "true",
                    "message": f"Successfully deleted consent with id {consent_id}",
                }
            )
        else:
            return jsonify(
                {
                    "deleted": "false",
                    "message": f"Requested consent with id {consent_id} "
                    f"was not deleted because it was not found in "
                    f"the database.",
                }
            )

    return consent_openapi_api
