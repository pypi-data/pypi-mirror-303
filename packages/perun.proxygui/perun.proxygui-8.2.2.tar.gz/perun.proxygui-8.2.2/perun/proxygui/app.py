import os

import jinja2
from cryptojwt.key_jar import init_key_jar
from flask import Flask, request, session
from flask_babel import Babel
from flask_pyoidc import OIDCAuthentication
from flask_pyoidc.provider_configuration import ClientMetadata, ProviderConfiguration
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from idpyoidc.client.configure import Configuration, RPHConfiguration
from idpyoidc.client.rp_handler import RPHandler
from idpyoidc.configure import create_from_config_file, Base
from perun.connector import Logger
from pymongo import MongoClient

from perun.proxygui.api.backchannel_logout_api import (
    construct_backchannel_logout_api_blueprint,
)
from perun.proxygui.api.ban_api import construct_ban_api_blueprint
from perun.proxygui.api.consent_api import construct_consent_api
from perun.proxygui.gui.gui import construct_gui_blueprint
from perun.proxygui.oauth import (
    configure_resource_protector,
)
from perun.proxygui.openapi.openapi import api_setup, compare_versions
from perun.utils.ConfigStore import ConfigStore
from perun.utils.CustomRPHandler import CustomRPHandler

BACKCHANNEL_LOGOUT_CFG = "backchannel-logout.yaml"

logger = Logger.get_logger(__name__)


def init_oidc_rp_handler() -> RPHandler:
    rp_conf = get_rp_config()

    key_jar = init_key_jar(**rp_conf.key_conf)
    key_jar.httpc_params = rp_conf.httpc_params

    public_path = rp_conf.key_conf["public_path"]
    norm_public_path = os.path.normpath(public_path)

    rph = CustomRPHandler(
        keyjar=key_jar,
        jwks_path=norm_public_path,
    )
    return rph


def get_rp_config() -> Base:
    # the entire filepath is required, not just the filename
    cfg_path = ConfigStore.get_config_path(BACKCHANNEL_LOGOUT_CFG)
    return create_from_config_file(
        Configuration,
        entity_conf=[{"class": RPHConfiguration, "attr": "rp"}],
        filename=cfg_path,
    )


def get_oidc_auth(cfg, app: Flask):
    oidc_cfg = cfg["oidc_provider"]

    app.config.update(OIDC_REDIRECT_URI=oidc_cfg["oidc_redirect_uri"])

    provider_configurations = {}
    for provider_name in ["oidc_provider", "mfa_provider", "without_mfa_provider"]:
        oidc_cfg = cfg[provider_name]
        client_metadata = ClientMetadata(
            client_id=oidc_cfg["client_id"],
            client_secret=oidc_cfg["client_secret"],
            post_logout_redirect_uris=oidc_cfg["post_logout_redirect_uris"],
        )
        provider_config = ProviderConfiguration(
            issuer=oidc_cfg["issuer"],
            client_metadata=client_metadata,
            auth_request_params={
                "acr_values": oidc_cfg.get("acr_values", ""),
                "prompt": oidc_cfg.get("prompt", ""),
                "scope": oidc_cfg.get("scopes", ["openid"]),
            },
        )
        provider_configurations[oidc_cfg["provider_name"]] = provider_config

    return OIDCAuthentication(provider_configurations, app)


def get_flask_app(cfg, openapi_version=None, return_with_api=False):
    def get_locale():
        if request.args.get("lang"):
            session["lang"] = request.args.get("lang")
        return session.get("lang", "en")

    app = Flask(__name__)
    app.jinja_loader = jinja2.FileSystemLoader("perun/proxygui/gui/templates")
    Babel(app, locale_selector=get_locale)
    app.secret_key = cfg["secret_key"]

    app.config["SERVER_NAME"] = cfg["host"]["server_name"]

    if "session_database" in cfg:
        app.config["SESSION_PERMANENT"] = True
        if cfg["session_database"]["session_type"] == "mongodb":
            app.config["SESSION_TYPE"] = "mongodb"
            app.config["SESSION_MONGODB"] = MongoClient(
                cfg["session_database"]["connection_string"]
            )
            app.config["SESSION_MONGODB_DB"] = cfg["session_database"]["database_name"]
            app.config["SESSION_MONGODB_COLLECT"] = cfg["session_database"][
                "collection_name"
            ]
        elif cfg["session_database"]["session_type"] == "sqlalchemy":
            app.config["SESSION_TYPE"] = "sqlalchemy"
            app.config["SQLALCHEMY_DATABASE_URI"] = cfg["session_database"][
                "connection_string"
            ]
            app.config["SESSION_SQLALCHEMY_TABLE"] = cfg["session_database"][
                "collection_name"
            ]
            session_db = SQLAlchemy(app)
            app.config["SESSION_SQLALCHEMY"] = session_db

        else:
            raise ValueError(
                "session_database.session_type must be mongodb or sqlalchemy"
            )
        Session(app)

    app, api = api_setup(app, openapi_version)

    # Optional GUI
    if isinstance(cfg.get("gui", None), dict):
        # initialize OIDC
        auth = get_oidc_auth(cfg.get("gui", None), app)

        @app.context_processor
        def inject_conf_var():
            gui_cfg = cfg.get("gui")
            html_dict = gui_cfg.get("html")
            if "css_framework" not in html_dict:
                cfg["css_framework"] = "bootstrap"

            if "bootstrap_color" not in html_dict:
                cfg["bootstrap_color"] = "primary"
            all_html_dict = {
                **html_dict,
                "general_translations": gui_cfg.get("general_translations"),
                "mfa_reset_translations": gui_cfg.get("mfa_reset").get(
                    "mfa_reset_translations"
                ),
            }

            return dict(cfg=all_html_dict, lang=get_locale())

        # Register GUI component
        app.register_blueprint(construct_gui_blueprint(cfg, auth))

    # Optional Ban API
    if isinstance(cfg.get("ban_api", None), dict):
        # Register API endpoints
        api.register_blueprint(construct_ban_api_blueprint(cfg))

    # Optional Consent API
    if isinstance(cfg.get("consent_api", None), dict):
        oauth_cfg = cfg["consent_api"]["oidc_provider"]
        configure_resource_protector(oauth_cfg)

        api.register_blueprint(construct_consent_api(cfg))

    # Optional Backchannel logout API
    if isinstance(cfg.get("backchannel_logout_api", None), dict):
        logout_cfg = ConfigStore.get_config(BACKCHANNEL_LOGOUT_CFG, False)
        if logout_cfg:
            api.register_blueprint(
                construct_backchannel_logout_api_blueprint(cfg, logout_cfg)
            )

            # Initialize the oidc_provider after views to be able to set correct urls
            app.rp_handler = init_oidc_rp_handler()

    if return_with_api:
        return app, api
    return app


# for uWSGI
def get_app(*args):
    cfg = ConfigStore.get_config()
    app = get_flask_app(cfg)
    return app(*args)


# for Flask OpenAPI generation in development
def get_openapi(*args):
    cfg = ConfigStore.get_config()
    _, compare_api = get_flask_app(cfg, return_with_api=True)
    new_version = compare_versions(cfg, compare_api)
    app = get_flask_app(cfg, new_version)
    return app


# for Flask OpenAPI generation
def get_openapi_dev(*args):
    cfg = ConfigStore.get_config()
    app = get_flask_app(cfg)
    return app


if __name__ == "__main__":
    cfg = ConfigStore.get_config()
    app = get_flask_app(cfg)

    app.run(
        host=cfg["host"]["ip-address"],
        port=cfg["host"]["port"],
        debug=cfg["host"]["debug"],
    )
