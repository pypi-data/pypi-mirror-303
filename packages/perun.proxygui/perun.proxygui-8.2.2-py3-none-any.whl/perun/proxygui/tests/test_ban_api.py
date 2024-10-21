import gzip
import io
import json
import mongomock
import tarfile
from http import HTTPStatus
from perun.proxygui.tests.shared_test_data import SHARED_TESTING_CONFIG, client
from unittest.mock import patch
from sqlalchemy import (
    Column,
    Integer,
)
from sqlalchemy.orm import declarative_base

Base = declarative_base()


# prevent client from being "unused" during static code analysis, it is injected to
# the tests upon launch
_ = client

BAN_IN_DB_1 = {
    "description": None,
    "facilityId": "1",
    "id": 1,
    "userId": "57986",
    "validityTo": "1670799600000",
}

BAN_IN_DB_2 = {
    "description": "Something serious",
    "facilityId": "1",
    "id": 2,
    "userId": "54321",
    "validityTo": "1670799600000",
}

BAN_NOT_IN_DB_1 = {
    "description": None,
    "facilityId": "1",
    "id": 3,
    "userId": "12345",
    "validityTo": "1670799600000",
}

BAN_NOT_IN_DB_2 = {
    "description": "Something serious again",
    "facilityId": "1",
    "id": 4,
    "userId": "5678",
    "validityTo": "1670799600000",
}

MOCK_CLIENT = mongomock.MongoClient()
BANS_IN_DB = [BAN_IN_DB_1, BAN_IN_DB_2]
BANS_NOT_IN_DB = [BAN_NOT_IN_DB_1, BAN_NOT_IN_DB_2]

BANNED_SUBJECT = "banned_subject"
ALLOWED_SUBJECT = "allowed_subject"

SATOSA_SESSIONS_COLLECTION = MOCK_CLIENT["satosa_database"]["ssp_collection"]
SATOSA_SESSIONS = [
    {"sub": BANNED_SUBJECT, "session_data": "1"},
    {"sub": BANNED_SUBJECT, "session_data": "2"},
    {"sub": ALLOWED_SUBJECT, "session_data": "1"},
    {"sub": ALLOWED_SUBJECT, "session_data": "2"},
]


class TestTable(Base):
    __tablename__ = "test_table"

    id = Column(Integer, primary_key=True)
    count = Column(Integer)


@patch("perun.proxygui.api.ban_api.get_ban_table")
@patch("perun.proxygui.api.ban_api.get_ban_engine")
def test_find_ban_ban_exists(mock_get_ban_engine, mock_get_ban_table, client):
    cursor_mock = (
        mock_get_ban_engine.return_value.begin.return_value.__enter__.return_value
    )
    cursor_mock.execute.return_value.fetchone.return_value._asdict.return_value = (
        BAN_IN_DB_1
    )

    mock_get_ban_table.return_value = TestTable.__table__

    response = client.get(f"/proxygui/bans/{BAN_IN_DB_1['id']}")
    result = json.loads(json.loads(response.data.decode()).get("_text", {}))

    for key, value in BAN_IN_DB_1.items():
        assert result.get(key) == value


@patch("perun.proxygui.api.ban_api.get_ban_table")
@patch("perun.proxygui.api.ban_api.get_ban_engine")
def test_find_ban_ban_doesnt_exist(mock_get_ban_engine, mock_get_ban_table, client):
    cursor_mock = (
        mock_get_ban_engine.return_value.begin.return_value.__enter__.return_value
    )
    cursor_mock.execute.return_value.fetchone.return_value._asdict.return_value = None
    mock_get_ban_table.return_value = TestTable.__table__

    not_in_db_ban_id = -1

    response = client.get(f"/proxygui/bans/{not_in_db_ban_id}")
    result = json.loads(json.loads(response.data.decode()).get("_text", {}))

    assert result == {}


@patch("perun.proxygui.api.ban_api.remove_outdated_bans_from_db")
@patch("perun.connector.AdaptersManager.get_user_attributes")
@patch("perun.proxygui.user_manager.UserManager.logout")
@patch("perun.proxygui.api.ban_api.is_ban_in_db")
@patch("perun.proxygui.api.ban_api.replace_one_in_db")
@patch("perun.proxygui.api.ban_api.get_ban_table")
@patch("perun.proxygui.api.ban_api.get_ban_engine")
def test_ban_user_all_users_already_banned(
    mock_get_ban_engine,
    mock_get_ban_table,
    mock_replace_one_in_db,
    mock_is_ban_in_db,
    mock_user_manager_logout,
    mock_get_user_attributes,
    mock_remove_outdated_bans_from_db,
    client,
):
    mock_get_user_attributes.return_value = {
        SHARED_TESTING_CONFIG["perun_person_principal_names_attribute"]: BANNED_SUBJECT
    }
    mock_remove_outdated_bans_from_db.return_value = None
    mock_replace_one_in_db.return_value = None
    mock_get_ban_table.return_value = TestTable.__table__
    mock_get_ban_engine.return_value.begin.return_value.__enter__.return_value = None
    mock_is_ban_in_db.return_value = True
    mock_user_manager_logout.return_value = None

    user_bans_in_db = {ban["userId"]: ban for ban in BANS_IN_DB}

    client.put(
        "/proxygui/bans",
        json=user_bans_in_db,
        headers={"Content-type": "application/json", "Accept": "application/json"},
    )
    assert not mock_user_manager_logout.called


@patch("perun.proxygui.api.ban_api.remove_outdated_bans_from_db")
@patch("perun.proxygui.user_manager.UserManager._delete_mitre_tokens")
@patch("perun.proxygui.user_manager.UserManager.logout")
@patch("perun.connector.AdaptersManager.get_user_attributes")
@patch("perun.proxygui.api.ban_api.replace_one_in_db")
@patch("perun.proxygui.api.ban_api.is_ban_in_db")
@patch("perun.proxygui.api.ban_api.get_ban_table")
@patch("perun.proxygui.api.ban_api.get_ban_engine")
def test_ban_user_add_new_bans(
    mock_get_ban_engine,
    mock_get_ban_table,
    mock_is_in_db,
    mock_replace_one_in_db,
    mock_get_user_attributes,
    mock_logout,
    mock_delete_mitre_tokens,
    mock_remove_outdated_bans_from_db,
    client,
):
    test_ban_db = BANS_IN_DB

    mock_delete_mitre_tokens.return_value = 0
    mock_get_user_attributes.return_value = {
        SHARED_TESTING_CONFIG["perun_person_principal_names_attribute"]: BANNED_SUBJECT
    }
    mock_get_ban_table.return_value = TestTable.__table__
    mock_get_ban_engine.return_value.begin.return_value.__enter__.return_value = None
    mock_remove_outdated_bans_from_db.return_value = None
    mock_replace_one_in_db.return_value = None
    mock_is_in_db.side_effect = lambda x, y, z: any(d["id"] == x for d in test_ban_db)

    all_user_bans = {ban["userId"]: ban for ban in BANS_IN_DB + BANS_NOT_IN_DB}

    def logout_from_test(user_id, include_refresh_tokens):
        test_ban_db.append(all_user_bans.get(user_id))

    number_of_bans_in_db = len(BANS_IN_DB)
    number_of_bans_not_in_db = len(BANS_NOT_IN_DB)

    mock_logout.side_effect = logout_from_test

    assert len(test_ban_db) == number_of_bans_in_db

    client.put("/proxygui/bans", json=all_user_bans)

    assert len(test_ban_db) == number_of_bans_in_db + number_of_bans_not_in_db

    for ban in BANS_IN_DB + BANS_NOT_IN_DB:
        assert ban in test_ban_db

    for ban in BANS_NOT_IN_DB:
        mock_logout.assert_any_call(user_id=ban["userId"], include_refresh_tokens=True)

    assert SATOSA_SESSIONS_COLLECTION.count_documents(
        {}
    ) == SATOSA_SESSIONS_COLLECTION.count_documents({"sub": ALLOWED_SUBJECT})
    assert SATOSA_SESSIONS_COLLECTION.find_one({"sub": BANNED_SUBJECT}) is None


def test_ban_users_tar_missing_file(
    client,
):
    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w|gz") as tar:
        text = b"facility file content"
        file_data = io.BytesIO(text)
        info = tarfile.TarInfo(name="FACILITY")
        info.size = len(text)
        tar.addfile(info, file_data)
    tar.name = "sent_data"

    buffer.seek(0)
    gzipped_data = gzip.compress(buffer.read())

    response = client.put(
        "/proxygui/bans/perun-idm",
        content_type="application/x-tar",
        data=gzipped_data,
    )
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


@patch("perun.proxygui.api.ban_api.replace_one_in_db")
@patch("perun.proxygui.user_manager.UserManager.logout")
@patch("perun.proxygui.api.ban_api.is_ban_in_db")
@patch("perun.proxygui.api.ban_api.remove_outdated_bans_from_db")
@patch("perun.proxygui.api.ban_api.get_ban_table")
@patch("perun.proxygui.api.ban_api.get_ban_engine")
def test_ban_users_tar_update(
    mock_get_ban_engine,
    mock_get_ban_table,
    mock_remove_outdated_bans_from_db,
    mock_is_in_db,
    mock_logout,
    mock_replace_one_in_db,
    client,
):
    test_db = []

    mock_get_ban_table.return_value = TestTable.__table__
    mock_get_ban_engine.return_value.begin.return_value.__enter__.return_value = None
    mock_remove_outdated_bans_from_db.return_value = None
    mock_is_in_db.side_effect = lambda x, y, z: any(d["id"] == x for d in test_db)
    mock_replace_one_in_db.retirn_value = None

    all_user_bans = {ban["userId"]: ban for ban in BANS_IN_DB + BANS_NOT_IN_DB}

    def logout_from_test(user_id, include_refresh_tokens):
        test_db.append(all_user_bans.get(user_id))

    mock_logout.side_effect = logout_from_test

    new_bans = {BAN_NOT_IN_DB_1["userId"]: BAN_NOT_IN_DB_1}

    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w|gz") as tar:
        text = json.dumps(new_bans).encode("utf-8")
        file_data = io.BytesIO(text)
        info = tarfile.TarInfo(name="./banned_facility_users")
        info.size = len(text)
        tar.addfile(info, file_data)
    tar.name = "data"

    buffer.seek(0)
    gzipped_data = gzip.compress(buffer.read())

    client.put(
        "/proxygui/bans/perun-idm",
        content_type="application/x-tar",
        data=gzipped_data,
    )

    assert len(test_db) == 1
