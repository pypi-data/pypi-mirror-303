import gzip
import io
import json
import tarfile
from http import HTTPStatus

import flask
import flask_smorest as fs
from bson.json_util import dumps
from flask import request, Response, jsonify
from perun.connector import Logger
from perun.proxygui.user_manager import UserManager
from perun.proxygui.openapi.openapi_data import openapi_route, apis_desc

from sqlalchemy import (
    MetaData,
    Engine,
    Table,
    select,
    delete,
    Connection,
    Column,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import declarative_base

logger = Logger.get_logger(__name__)
Base = declarative_base()


class MissingInformationError(Exception):
    pass


class Ban(Base):
    __tablename__ = "ban_table"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    facilityId = Column(String)
    userId = Column(String)
    validityTo = Column(String)


def get_ban_engine(user_manager: UserManager) -> Engine:
    return user_manager.database_service.get_postgres_engine("ban_database")


def get_ban_table(user_manager: UserManager, engine: Engine, cfg) -> Table:
    table = cfg.get("ban_database", {}).get("table_name", None)
    if table is None:
        Ban.__table__.create(bind=engine, checkfirst=True)
        table = Ban.__tablename__
    return user_manager.database_service.get_postgres_table(engine, table)


def get_ban_from_db(engine, user_manager, ban_id, ban_cfg):
    with engine.begin() as cnxn:
        meta_data = MetaData()
        meta_data.reflect(engine)

        ban_table = get_ban_table(user_manager, engine, ban_cfg)

        query = select(ban_table).where(ban_table.c.id == int(ban_id)).limit(1)
        response = cnxn.execute(query).fetchone()._asdict()

        return response


def remove_outdated_bans_from_db(banned_users, ban_table: Table, cnxn: Connection):
    current_ban_ids = [ban["id"] for ban in banned_users.values()]
    query = delete(ban_table).where(ban_table.c.id not in current_ban_ids)
    result = cnxn.execute(query)
    logger.info(f"{result.rowcount} outdated bans were successfully deleted.")


def is_ban_in_db(ban_id: int, cnxn: Connection, ban_table: Table) -> bool:
    query = select(ban_table).where(ban_table.c.id == int(ban_id)).limit(1)
    response = [r._asdict() for r in cnxn.execute(query).fetchall()]
    return len(response) > 0


def replace_one_in_db(ban_id: int, cnxn: Connection, ban_table: Table, ban):
    if (
        not ban.get("description")
        or not ban.get("facilityId")
        or not ban.get("userId")
        or not ban.get("validityTo")
    ):
        raise MissingInformationError("Missing ban info in the request.")
    ban_dict = {
        key: ban[key]
        for key in ["description", "facilityId", "userId", "validityTo"]
        if key in ban
    }
    query = (
        insert(ban_table)
        .values(id=ban_id, **ban_dict)
        .on_conflict_do_update(constraint="ban_table_pkey", set_=ban_dict)
    )
    cnxn.execute(query)


def construct_ban_api_blueprint(cfg):
    ban_openapi_api = fs.Blueprint(
        "Ban API",
        __name__,
        url_prefix="/proxygui",
        description=apis_desc.get("ban", ""),
    )
    BAN_CFG = cfg.get("ban_api")

    USER_MANAGER = UserManager(BAN_CFG)
    UPLOAD_FILE_MAX_SIZE = int(BAN_CFG.get("max_ban_upload_filesize"))

    # Endpoints
    @openapi_route("/bans", ban_openapi_api)
    def update_banned_users() -> Response:
        try:
            process_update(request.get_json())
            logger.info("Banned users successfully updated.")
            response = flask.Response()
            response.headers["Cache-Control"] = "public, max-age=0"
            response.status_code = HTTPStatus.NO_CONTENT
        except MissingInformationError:
            error = "Banned users update failed - bad json in the request."
            logger.warning(error)
            flask.abort(HTTPStatus.NOT_FOUND, error)

        return response

    @openapi_route("/bans/perun-idm", ban_openapi_api)
    def update_banned_users_generic() -> Response:
        if request.content_length > UPLOAD_FILE_MAX_SIZE:
            logger.warn(
                f"Request too large: "
                f"{str((request.content_length // 1024) // 1024)} MB"
            )
            response = flask.make_response(
                "Request too large!", HTTPStatus.REQUEST_ENTITY_TOO_LARGE
            )
            response.headers["Cache-Control"] = "public, max-age=0"
            return response

        banned_users = None
        banned_users_tar_filepath = "./banned_facility_users"
        io_bytes = io.BytesIO(request.get_data())
        gzip_file = gzip.GzipFile(fileobj=io_bytes)
        try:
            with tarfile.open(fileobj=gzip_file) as tar:
                for tarinfo in tar:
                    if tarinfo.isreg() and tarinfo.name == banned_users_tar_filepath:
                        ban_file = tarinfo.path
                        with tar.extractfile(ban_file) as f:
                            content = f.read()
                            banned_users = json.loads(content)
        except Exception as ex:
            logger.warn("Could not parse banned users data: ", ex)
            return flask.make_response(
                f"Could not parse banned users data: {ex}",
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )

        if banned_users is None:
            logger.warn("Banned users file not found in the request.")
            response = flask.make_response(
                "Banned users file not found in the request.",
                HTTPStatus.UNPROCESSABLE_ENTITY,
            )
            response.headers["Cache-Control"] = "public, max-age=0"
            return response

        try:
            process_update(banned_users)
            logger.info("Banned users successfully updated.")
            response = flask.Response()
            response.headers["Cache-Control"] = "public, max-age=0"
            response.status_code = HTTPStatus.NO_CONTENT
        except MissingInformationError:
            error = "Banned users update failed - bad json in the request."
            logger.warning(error)
            flask.abort(HTTPStatus.NOT_FOUND, error)

        return response

    def process_update(banned_users) -> None:
        engine = get_ban_engine(USER_MANAGER)

        with engine.begin() as cnxn:
            meta_data = MetaData()
            meta_data.reflect(engine)

            ban_table = get_ban_table(USER_MANAGER, engine, BAN_CFG)

            remove_outdated_bans_from_db(banned_users, ban_table, cnxn)

            for user_id, ban in banned_users.items():
                if not user_id or not ban or not ban.get("id"):
                    raise MissingInformationError(
                        "Missing user_id or ban info in the request."
                    )
                if not is_ban_in_db(int(ban["id"]), cnxn, ban_table):
                    USER_MANAGER.logout(user_id=user_id, include_refresh_tokens=True)
                replace_one_in_db(int(ban["id"]), cnxn, ban_table, ban)

    @openapi_route("/bans/<string:ban_id>", ban_openapi_api)
    def find_ban(ban_id: str) -> str:
        engine = get_ban_engine(USER_MANAGER)
        response = get_ban_from_db(engine, USER_MANAGER, ban_id, BAN_CFG)

        return jsonify({"_text": (dumps({} if not response else response))})

    return ban_openapi_api
