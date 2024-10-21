import copy
from http import HTTPStatus
from urllib import parse
from uuid import uuid4

import flask
import yaml
from flask import (
    Blueprint,
    request,
    url_for,
    render_template,
    make_response,
    jsonify,
    session,
    redirect,
)
from flask_babel import get_locale, gettext
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.user_session import UserSession
from perun.connector.utils import Logger

from perun.proxygui.api.heuristic_api import AuthEventLoggingQueries
from perun.proxygui.jwt import SingletonJWTServiceProvider
from perun.proxygui.logout_manager import LogoutManager
from perun.proxygui.user_manager import UserManager
from perun.utils.CustomExceptions import InvalidJWTError, UserNotExistsException
from perun.utils.Notification import NotificationType
from perun.utils.consent_framework.consent_manager import ConsentManager

logger = Logger.Logger.get_logger(__name__)


def ignore_claims(ignored_claims, claims):
    result = dict()

    for claim in claims:
        if claim not in ignored_claims:
            result[claim] = claims[claim]

    return result


def check_scope_claim(auth_group_name, cfg):
    user_session = UserSession(flask.session, cfg.get("provider_name"))

    # Load athoriyation from config
    claim_cfg = cfg.get("authorization_claims", {}).get(auth_group_name, {})
    if claim_cfg == {}:
        return False

    claim_cfg_name = claim_cfg.get("name", None)
    claim_cfg_value = claim_cfg.get("value", None)
    if claim_cfg_name is None or claim_cfg_value is None:
        return False

    # Get specific claim from userinfo
    session_scope_claim = user_session.userinfo.get(claim_cfg_name, None)

    if session_scope_claim is None:
        return False

    return (
        claim_cfg_value in session_scope_claim
        if isinstance(session_scope_claim, list)
        else claim_cfg_value == session_scope_claim
    )


def has_ongoing_logouts(services) -> bool:
    for service in services:
        if service.get("iframe_src", False):
            return True

    return False


def construct_gui_blueprint(cfg, auth: OIDCAuthentication):
    gui = Blueprint(
        "gui",
        __name__,
        template_folder="templates",
        url_prefix="/proxygui",
        static_folder="static",
    )

    GUI_CFG = cfg.get("gui")
    REDIRECT_URL = GUI_CFG["redirect_url"]
    MFA_CFG = GUI_CFG["mfa_provider"]
    WITHOUT_MFA_CFG = GUI_CFG["without_mfa_provider"]

    if GUI_CFG.get("consent", None):
        consent_db_manager = ConsentManager(GUI_CFG)
    user_manager = UserManager(GUI_CFG)

    jwt_service = SingletonJWTServiceProvider.get_provider().get_service()
    logout_manager = LogoutManager(GUI_CFG)
    auth_event = AuthEventLoggingQueries(GUI_CFG)

    @gui.route("/authorization/<request_jwt>", methods=["POST"])
    def authorization(request_jwt):
        try:
            message = jwt_service.verify_jwt(request_jwt)
        except InvalidJWTError as e:
            return make_response(
                jsonify({gettext("fail"): f"JWT validation failed with error: '{e}'"}),
                400,
            )
        email = message.get("email")
        service = message.get("service")
        registration_url = message.get("registration_url")
        if not email or not service:
            return make_response(
                jsonify({gettext("fail"): gettext("Missing request parameter")}),
                400,
            )
        return render_template(
            "authorization.html",
            email=email,
            service=service,
            registration_url=registration_url,
        )

    @gui.route("/sp-authorization/<request_jwt>", methods=["POST"])
    def sp_authorization(request_jwt):
        try:
            message = jwt_service.verify_jwt(request_jwt)
        except InvalidJWTError as e:
            return make_response(
                jsonify({gettext("fail"): f"JWT validation failed with error: '{e}'"}),
                400,
            )
        email = message.get("email")
        service = message.get("service")
        registration_url = message.get("registration_url")
        return render_template(
            "SPAuthorization.html",
            email=email,
            service=service,
            registration_url=registration_url,
        )

    # Logout
    # ==================================================================================
    if GUI_CFG.get("logout"):
        logout_cfg = GUI_CFG.get("logout")
        proxy_logout_texts = {
            "title": logout_cfg.get("proxy_logout_title", ""),
            "proxy_name": logout_cfg.get("proxy_name", ""),
        }

        @gui.route("/logout-system", methods=["POST", "GET"])
        def logout():
            ssp_session_id = request.cookies.get("SimpleSAMLSessionID")

            logger.debug(f"Logout call for SimpleSAMLSessionID: {ssp_session_id}")
            # todo - dbs will contain user_id and won't need to be converted in the
            #  future
            sub = user_manager.get_user_id_by_ssp_session_id(ssp_session_id)

            if ssp_session_id is None or sub is None:
                return render_template("MissingAuth.html")

            session["sub"] = sub

            resp = make_response(
                render_template(
                    "logout-proxy.html",
                    proxy_logout_texts=proxy_logout_texts,
                )
            )
            return resp

        @gui.route("/logout-services", methods=["POST", "GET"])
        def logout_services():
            ssp_session_id = request.cookies.get("SimpleSAMLSessionID")
            sub = session.get("sub")

            (
                valid_request,
                client_id,
                rp_sid,
                issuer,
                logout_params,
            ) = logout_manager.validate_request_and_extract_params(
                ssp_session_id, request
            )

            if valid_request:
                user_manager.logout_from_service_op(sub, ssp_session_id, client_id)

            device_active_clients = user_manager.get_active_client_ids_for_user(sub)
            session_active_clients = user_manager.get_active_client_ids_for_session(
                ssp_session_id
            )

            rp_names = user_manager.get_all_rp_names()
            logged_out_service = (
                {
                    "from_devices": rp_sid is None,
                    # user might have been logged out for all devices
                    "labels": rp_names.get(client_id, client_id),
                    "client_id": client_id,
                }
                if client_id is not None
                else {}
            )

            session_services = logout_manager.complete_service_names(
                session_active_clients, rp_names
            )
            device_services = logout_manager.complete_service_names(
                device_active_clients, rp_names
            )
            session["logout_params"] = logout_params if logout_params else {}
            session["init_logged_out_service"] = logged_out_service
            session["init_issuer"] = issuer  # todo - we probably don't need to save it

            has_matching_services = sorted(
                [service_name.get("en") for service_name in session_services]
            ) == sorted([service_name.get("en") for service_name in device_services])
            resp = make_response(
                render_template(
                    "logout.html",
                    logged_out_service=logged_out_service,
                    session_services=session_services,
                    device_services=device_services,
                    has_matching_services=has_matching_services,
                    proxy_logout_texts=proxy_logout_texts,
                )
            )
            session["ssp_session_id"] = ssp_session_id
            resp.delete_cookie("SimpleSAMLSessionID")

            return resp

        @gui.route("/logout-canceled")
        def logout_canceled():
            return render_template(
                "logout-canceled.html",
            )

        @gui.route("/logout-state")
        def logout_state():
            if session.get("logout_params") is None:
                # at least empty dict should be set, or logout endpoint was not visited
                return redirect(url_for("gui.logout", _external=True))

            ssp_session_id = session.get("ssp_session_id")
            # todo - dbs will contain user_id and won't need to be converted in the
            #  future
            sub = user_manager.get_user_id_by_ssp_session_id(ssp_session_id)

            if ssp_session_id is None or sub is None:
                return render_template("MissingAuth.html")

            include_all_devices = request.args.get("from_devices", False)
            include_all_devices = include_all_devices in ["True", True, "true"]

            if include_all_devices:
                active_clients = user_manager.get_active_client_ids_for_user(sub)
                unique_client_issuer_clients = []
                for client_id, sid, issuer, name_id in active_clients:
                    found = next(
                        filter(
                            lambda x: x[0] == client_id and x[2] == issuer,
                            unique_client_issuer_clients,
                        ),
                        None,
                    )
                    (
                        unique_client_issuer_clients.append(
                            (client_id, sid, issuer, name_id)
                        )
                        if not found
                        else None
                    )
                    active_clients = unique_client_issuer_clients
            else:
                active_clients = user_manager.get_active_client_ids_for_session(
                    ssp_session_id
                )

            rp_names = user_manager.get_all_rp_names()
            # todo - jazyky brát z config option languages - brát průnik,
            #  issuer bude mapa {issuer: pretty_name}
            # todo - pěkná funkce na vyčítání (fallback když je jenom japonská verze
            #  atd...)
            service_configs = logout_manager.services_configuration
            logout_requests = [
                logout_manager.prepare_logout_request(
                    service_configs,
                    client_id,
                    name_id,
                    rp_names.get(client_id, {"en": client_id, "cs": client_id}),
                    issuer,
                    rp_sid if include_all_devices else None,
                ).to_dict()
                for (client_id, rp_sid, issuer, name_id) in active_clients
            ]
            session["logout_requests"] = logout_requests
            init_logged_out_client_id = session["init_logged_out_service"].get(
                "client_id"
            )
            session["init_logged_out_service"]["logback_url"] = (
                service_configs.get("RPS", {})
                .get(init_logged_out_client_id, {})
                .get("logback_url")
            )

            main_issuer = cfg.get("issuers", [{}])[0].get("issuer")
            if not main_issuer:
                logger.error("Main issuer not set!")
                return make_response(
                    jsonify({gettext("fail"): "Invalid endpoint configuration."}),
                    400,
                )
            user_id = user_manager.sub_to_user_id(sub, main_issuer)
            if not user_id:
                return render_template("MissingAuth.html")
            user_manager.logout(
                user_id=user_id,
                session_id=ssp_session_id if include_all_devices else None,
                include_refresh_tokens=include_all_devices,
            )

            if include_all_devices:
                session_services = []
                device_services = logout_requests
            else:
                session_services = logout_requests
                device_services = []

            has_ongoing_session_logouts = has_ongoing_logouts(session_services)
            has_ongoing_device_logouts = has_ongoing_logouts(device_services)

            has_any_ongoing_logouts = (
                has_ongoing_session_logouts or has_ongoing_device_logouts
            )

            session["successful_logout_services"] = []
            session["logout_requests"] = logout_requests

            resp = make_response(
                render_template(
                    "logout-state.html",
                    session_services=session_services,
                    device_services=device_services,
                    has_ongoing_logouts=has_any_ongoing_logouts,
                    proxy_logout_texts=proxy_logout_texts,
                )
            )
            return resp

        @gui.route("/logout-post")
        def post_logout():
            logout_params = session.get("logout_params")
            init_logged_out_service = session.get("init_logged_out_service")

            successful_logout_services = session.get("successful_logout_services", [])
            logout_requests = session.get("logout_requests", [])

            unknown_status_logout_services = [
                req for req in logout_requests if req not in successful_logout_services
            ]

            session.clear()

            if (
                logout_params is None or init_logged_out_service is None
            ):  # can be {} but not None (wrong flow then)
                return render_template("MissingAuth.html")

            if "post_logout_redirect_uri" in logout_params:
                url = logout_params["post_logout_redirect_uri"]
                if "state" in logout_params:
                    state = parse.quote(logout_params["state"])
                    url = f"{url}?{state}" if "?" not in url else f"{url}&{state}"
                return redirect(url)

            return render_template(
                "logout-post.html",
                init_logged_out_service=init_logged_out_service,
                successful_logout_services=successful_logout_services,
                unknown_status_logout_services=unknown_status_logout_services,
                proxy_logout_texts=proxy_logout_texts,
            )

        @gui.route("/logout-iframe-callback")
        def logout_iframe_callback():
            request_id = request.args.get("request_id")
            logout_requests = session["logout_requests"]

            current_request = next(
                (r for r in logout_requests if str(r["id"]) == request_id), None
            )

            if current_request is None:
                response = False
            else:
                req = logout_manager.deserialize_request(current_request)
                response = req.logout()

            successful_logout_services = session.get("successful_logout_services", [])

            if response:
                successful_logout_services.append(current_request)

            session["successful_logout_services"] = successful_logout_services

            return render_template(
                "logout-iframe.html",
                result="success" if response else response,
            )

        @gui.route("/logout-saml-callback/<path:issuer_id>")
        def logout_saml_callback(issuer_id):
            if (not issuer_id.startswith("https://")) and issuer_id.startswith(
                "https:/"
            ):
                issuer_id = issuer_id.replace("https:/", "https://", 1)

            request_ok = logout_manager.check_saml_callback(request, issuer_id)

            successful_logout_services = session.get("successful_logout_services", [])

            if request_ok:
                successful_logout_services.append(request)

            session["successful_logout_services"] = successful_logout_services

            return render_template(
                "logout-iframe.html",
                result="success" if request_ok else "request invalid",
            )

    # Testing
    # ==================================================================================
    if GUI_CFG.get("is_testing_sp", None):

        @gui.route("/is-testing-sp")
        def is_testing_sp():
            return render_template(
                "IsTestingSP.html",
                redirect_url=REDIRECT_URL,
            )

    # Consent
    # ==================================================================================
    if GUI_CFG.get("consent", None):

        @gui.route("/consent-requests/<request_jwt>")
        def consent(request_jwt):
            try:
                ticket = jwt_service.verify_jwt(request_jwt)
            except InvalidJWTError as e:
                return make_response(
                    jsonify(
                        {gettext("fail"): f"JWT validation failed with error: '{e}'"}
                    ),
                    400,
                )
            data = consent_db_manager.fetch_consent_request(ticket)
            if not ticket:
                return make_response(
                    jsonify({gettext("fail"): gettext("received invalid ticket")}),
                    400,
                )

            months_valid = GUI_CFG["consent"]["months_valid"]
            session["id"] = data["id"]
            session["state"] = uuid4().urn
            session["redirect_endpoint"] = data["redirect_endpoint"]
            session["attr"] = ignore_claims(
                GUI_CFG["consent"]["ignored_claims"], data["attr"]
            )
            session["user_id"] = data["user_id"]
            session["locked_attrs"] = data.get("locked_attrs")
            session["requester_name"] = data["requester_name"]
            session["month"] = months_valid

            warning = GUI_CFG["consent"].get("warning", None)
            with open(
                GUI_CFG["consent"]["attribute_config_path"],
                "r",
                encoding="utf8",
            ) as ymlfile:
                attr_config = yaml.safe_load(ymlfile)

            return render_template(
                "ConsentRegistration.html",
                cfg=cfg,
                attr_config=attr_config,
                released_claims=copy.deepcopy(session["attr"]),
                locked_claims=session["locked_attrs"],
                requester_name=session["requester_name"],
                months=months_valid,
                data_protection_redirect=data["data_protection_redirect"],
                warning=warning,
            )

    # MFA
    # ==================================================================================
    if GUI_CFG.get("mfa_reset", None):

        @gui.route("/mfa/reset/assisted/verify/<mfa_reset_jwt>")
        @auth.oidc_auth(WITHOUT_MFA_CFG["provider_name"])
        def mfa_reset_verify(mfa_reset_jwt):
            try:
                reset_request = jwt_service.verify_jwt(mfa_reset_jwt)
            except InvalidJWTError:
                return render_template(
                    "MfaResult.html",
                    title="request_fail_title",
                    info="request_fail_info",
                )
            requester_email = reset_request.get("requester_email")
            requester_id = reset_request.get("requester_id")
            user_manager.forward_mfa_reset_request(requester_id, requester_email)
            return render_template(
                "MfaResult.html",
                title="request_success_title",
                info="request_success_info",
            )

        @gui.route("/mfa/reset/assisted/confirm", methods=["POST"])
        @auth.oidc_auth(WITHOUT_MFA_CFG["provider_name"])
        def send_mfa_reset_emails():
            user_session = UserSession(flask.session, WITHOUT_MFA_CFG["provider_name"])
            sub = user_session.userinfo.get("sub")
            issuer = WITHOUT_MFA_CFG["issuer"]
            user_id = user_manager.sub_to_user_id(sub, issuer)
            if not user_id:
                return (
                    f"No corresponding user found for sub: '{sub}'",
                    HTTPStatus.NOT_FOUND,
                )

            locale = get_locale().language
            preferred_email = user_manager.handle_mfa_reset(
                user_id,
                locale,
                NotificationType.VERIFICATION,
            )
            return render_template(
                "MfaResetEmailSent.html",
                email=preferred_email,
            )

        @gui.route("/mfa/reset/assisted")
        @auth.oidc_auth(WITHOUT_MFA_CFG["provider_name"])
        def mfa_reset_init():
            return render_template(
                "MfaResetInitiated.html",
                redirect_url=REDIRECT_URL,
                referrer=request.referrer or "/",
                next_action=url_for("gui.send_mfa_reset_emails"),
            )

        @gui.route("/mfa/reset/delegated/confirm", methods=["POST"])
        @auth.oidc_auth(MFA_CFG["provider_name"])
        def mfa_perform_delegated_reset():
            if not session.get("mfa_reset_visited"):
                # force user to confirm this action
                return redirect(url_for("gui.mfa_delegated_reset"))
            user_session = UserSession(flask.session, MFA_CFG["provider_name"])
            username = user_session.id_token.get("sub")
            locale = get_locale().language
            tokens = logout_manager.remove_mfa_tokens(username)

            if tokens > 0:
                issuer = MFA_CFG["issuer"]
                user_id = user_manager.sub_to_user_id(username, issuer)
                user_manager.handle_mfa_reset(
                    user_id,
                    locale,
                    NotificationType.CONFIRMATION,
                )
                return render_template(
                    "MfaResult.html",
                    title="delegated_successful_title",
                    info="delegated_successful_info",
                )
            else:
                session["mfa_reset_success"] = True
                return render_template(
                    "MfaResult.html",
                    title="delegated_failed_title",
                    info="delegated_failed_info",
                )

        @gui.route("/mfa/reset/delegated")
        @auth.oidc_auth(MFA_CFG["provider_name"])
        def mfa_delegated_reset_init():
            session["mfa_reset_visited"] = True
            return render_template(
                "MfaResetInitiated.html",
                redirect_url=REDIRECT_URL,
                referrer=request.referrer or "/",
                next_action=url_for("gui.mfa_perform_delegated_reset"),
            )

    # Heuristic
    # ==================================================================================
    if GUI_CFG.get("heuristic_page", None):

        @gui.route("/heuristics")
        @auth.oidc_auth(MFA_CFG["provider_name"])
        def heuristics():
            if not check_scope_claim("heuristic_pages", MFA_CFG):
                return "User does not have access to this page", HTTPStatus.FORBIDDEN

            user_id = request.args.get("user_id")
            if not user_id:
                return render_template(
                    "HeuristicData.html",
                    redirect_url=REDIRECT_URL,
                    selected=False,
                    user_not_exists=False,
                )

            try:
                user_id = int(user_id)
            except ValueError:
                return (
                    f"Provided user ID: '{user_id}' could not be converted to an "
                    f"integer"
                ), HTTPStatus.BAD_REQUEST

            try:
                name = user_manager.get_user_name(user_id)
            except UserNotExistsException:
                user_not_exists_message = f"User with ID {user_id} does not exist."
                return render_template(
                    "HeuristicData.html",
                    redirect_url=REDIRECT_URL,
                    selected=False,
                    user_not_exists=True,
                    user_not_exists_message=user_not_exists_message,
                )

            auth_event.get_auth_logs(user_id)

            return render_template(
                "HeuristicData.html",
                redirect_url=REDIRECT_URL,
                selected=True,
                user_not_exists=False,
                user=user_id,
                name=name,
                last_n_times=auth_event.get_last_n_times(),
                user_agents=auth_event.get_unique_user_agents(),
                last_n_cities=auth_event.get_last_n_cities(),
                sps=auth_event.get_last_n_services(),
                ips=auth_event.get_last_n_ips(),
            )

    @gui.route("/oidc-error")
    def display_oidc_error_screen():
        return render_template(
            "OidcError.html",
            title="oidc_error_title",
            info="oidc_error_info",
        )

    # Process error during OIDC authentication and display helpful information to
    # user. Handled using GUI endpoint redirect to locate static folder successfully.
    @auth.error_view
    def handle_oidc_error(error=None, error_description=None):
        logger.debug(
            f"An error has occurred during OIDC authentication process: "
            f"'{error}' with following description: '{error_description}'"
        )

        return redirect(url_for("gui.display_oidc_error_screen"))

    return gui
