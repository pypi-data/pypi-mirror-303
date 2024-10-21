from http import HTTPStatus

from perun.proxygui.openapi.schemas.response_schemas import (
    response_schema,
    redirect_schema,
    # consent_attrs_schema, # Not used yed - need to be more specific in attribute description
    string_schema,
    user_consents_schema,
    delete_consent_schema,
)

from perun.proxygui.openapi.schemas.arguments_schemas import (
    file_input_schema,
    ban_id_argument_schema,
    backchannel_oidc_schema,
    consent_id_argument_schema,
    jwt_arguments_schema,
)


def load_response(src: dict):
    if src == {}:
        return None
    data = {
        "schema": src.get("schema", None),
        "example": src.get("example", None),
        "description": src.get("description", None),
    }
    return src.get("status", HTTPStatus.OK), {
        k: v for k, v in data.items() if v is not None
    }


def load_argument(src: dict):
    data = {
        "location": src.get("location", None),
        "description": src.get("description", None),
        "as_kwargs": True,
    }

    return src.get("schema", None), {k: v for k, v in data.items() if v is not None}


# Loding endpoint data from `data` dictionary
def load_data(src: dict):
    # Load documentation params and remove `None` ones
    doc_params = {
        "description": src.get("desc"),
        "summary": src.get("sum"),
        "security": src.get("security", None),
    }
    not_none_doc_params = {k: v for k, v in doc_params.items() if v is not None}

    # Load response and alterative response
    response = load_response(src.get("response", {}))
    alt_responses = [load_response(x) for x in src.get("alt_responses", [])]

    # Load two types of arguments path and non-path
    arguments = [
        load_argument(x)
        for x in src.get("arguments", [])
        if x.get("location") != "path"
    ]
    path_arguments = [
        x for x in src.get("arguments", []) if x.get("location") == "path"
    ]
    return not_none_doc_params, response, alt_responses, arguments, path_arguments


def openapi_route(route, blueprint):
    def testResponseApi(fn):
        def wrapper(**kwargs):
            nonlocal fn
            return fn(**kwargs)

        _data = data.get(route, {})
        doc_params, response, alt_responses, arguments, path_arguments = load_data(
            _data
        )

        # Decorators in raw form
        #
        # Response ---- @bp.response()
        if response != {} and response is not None:
            wrapper = blueprint.response(response[0], **response[1])(wrapper)
        # Alt responses ----@bp.alt_response
        for alt_res in alt_responses:
            if alt_res[1] != {} and alt_res[0] is not None:
                wrapper = blueprint.alt_response(alt_res[0], **alt_res[1])(wrapper)

        # Arguments ---- @bp.arguments
        for argument in arguments:
            wrapper = blueprint.arguments(argument[0], **argument[1])(wrapper)

        # Arguments in endpoint route ---- @bp.arguments
        for path_arg in path_arguments:
            wrapper = blueprint.arguments(
                path_arg.get("schema"), location="path", as_kwargs=True
            )(wrapper)

        # Documentation --- @bp.doc
        wrapper = blueprint.doc(**doc_params)(wrapper)
        # Endpoint route --- @bp.route
        wrapper = blueprint.route(route, methods=_data.get("methods", ["GET"]))(wrapper)
        return wrapper

    return testResponseApi


TODO_DESCRIPTION = "todo description"

# Formatting tips for descriptions: https://www.baeldung.com/swagger-format-descriptions
apis_desc = {
    # Consent API description
    "consent": """
This API handles consents - checks if any consent
    was given by the user and asks him to give a new one if not.
    API is connected to GUI where user can choose which attributes
    are to be consented. This API is strongly based 
    on [CMservice](https://github.com/its-dirg/CMservice). Some of the differences:

- GUI
- usage of MongoDB
- user_id and requester_name are sent from micro_service and are part of
    the consent stored in the database
- we can define attributes which are ignored (in the config)
""",
    # Ban API description
    "ban": """
Provides management of Perun user bans. A banned user can not log in to the system.
""",
    # Backchannel logout API description
    "backchannel_logout": """
Performs [OIDC Back-Channel Logout 1.0](https://openid.net/specs/openid-connect-backchannel-1_0.html) in the role of RP.
""",
}


data = {
    # ------------ Backchannel logout -----------------------------------------
    "/backchannel-logout": {
        "methods": ["POST"],
        "desc": """
The logout token **must** include an attribute `sub` containing
subject id
(id of the user to be logged out). It **may** also include `sid` containing an id of
a specific session of user identified by `sub`. In case the request contains `sid`
and the session with given `sid` exists and belongs to the user with provided `sub`, it
will be revoked, otherwise nothing happens. If **only** `sub` is provided, **all** the
sessions of the user with given `sub` will be revoked. If the user doesn't exist,
nothing happens.

Calling this endpoint revokes user's SSP sessions and Mitre tokens.
Refresh tokens will stay intact as per [OIDC standard](https://openid.net/specs/openid-connect-backchannel-1_0.html#BCActions).

**Example logout token**:

```json
{
  "iss": "https://server.example.com",
  "sub": "123456@user",
  "sid": "2d1a...5264be",
  "aud": "s6BhdRkqt3",
  "iat": 1471566154,
  "jti": "bWJq",
  "events": {
      "http://schemas.openid.net/event/backchannel-logout": {}
  }
}
```

(sid is optional)

**Input
arguments:** [OIDC Logout Token](https://openid.net/specs/openid-connect-backchannel-1_0.html#LogoutToken)
in the request body.
""",
        "sum": "",
        "response": {
            "status": HTTPStatus.NO_CONTENT,
            "schema": response_schema,
            "description": "`HTTP No Content [204]` indicating a successful logout",
        },
        "alt_responses": [
            {
                "status": HTTPStatus.BAD_REQUEST,
                "schema": response_schema,
                "description": "`HTTP Bad Request [400]` and an error message in the response body if the logout wasn't performed successfully",
            }
        ],
        "arguments": [
            {
                "location": "form",
                "schema": backchannel_oidc_schema,
            }
        ],
    },
    # ------------ Consent API ------------------------------------------------
    "/verify/<string:consent_id>": {
        "desc": "page",
        "sum": "verify",
        "response": {
            "status": HTTPStatus.OK,
            # "schema": consent_attrs_schema
        },
        "alt_response": [
            {"status": HTTPStatus.UNAUTHORIZED, "schema": response_schema}
        ],
        "arguments": [{"location": "path", "schema": consent_id_argument_schema}],
    },
    # ----------------------------------------
    "/creq/<string:jwt>": {
        "methods": ["GET", "POST"],
        "desc": "creq-page",
        "sum": "creq",
        "security": [{"bearerAuthJWT": []}],
        "response": {
            "status": HTTPStatus.OK,
            # "schema": consent_attrs_schema
        },
        "alt_responses": [
            {"status": HTTPStatus.BAD_REQUEST, "schema": response_schema}
        ],
        "arguments": [{"location": "path", "schema": jwt_arguments_schema}],
    },
    # ----------------------------------------
    "/save_consent": {
        "desc": "save_consent_page",
        "sum": "save_consent",
        "response": {
            "status": 302,
            "schema": redirect_schema,
        },
        "alt_responses": [
            {"status": HTTPStatus.FORBIDDEN, "schema": response_schema},
            {"status": HTTPStatus.BAD_REQUEST, "schema": response_schema},
        ],
    },
    # ----------------------------------------
    "/users/me/consents": {
        "methods": ["GET"],
        "desc": "Returns list of Consent objects",
        "sum": "consents",
        "security": [{"oAuthScheme": []}],
        "response": {
            "status": HTTPStatus.OK,
            "schema": user_consents_schema,
        },
        "alt_responses": [
            {"status": HTTPStatus.INTERNAL_SERVER_ERROR, "schema": response_schema}
        ],
    },
    # ----------------------------------------
    "/users/me/consents/<string:consent_id>": {
        "methods": ["DELETE"],
        "desc": "page",
        "sum": "delete_consents",
        "security": [{"oAuthScheme": []}],
        "response": {
            "status": HTTPStatus.OK,
            "schema": delete_consent_schema,
        },
        "arguments": [{"location": "path", "schema": consent_id_argument_schema}],
    },
    # ------------ Ban API ----------------------------------------------------
    "/bans": {
        "methods": ["PUT"],
        "desc": """
This endpoint adds all user bans provided in the request input data to the database. This effectively
bans the Perun users from logging in to the system. If the user is already banned, their ban is replaced with the latest
one (the one currently provided in the request).

Calling this endpoint revokes user's SSP sessions, Mitre tokens and
refresh tokens.

**Example ban:**

```json
{
    "description": "Misuse of resources.",
    "facilityId": "1",
    "id": 1,
    "userId": "12345",
    "validityTo": "1670799600000",
}
```

Here, `id` is the ban ID and `validityTo` is the time when the ban expires represented as a UNIX timestamp.
""",
        "sum": "update_banned_users",
        "response": {
            "status": HTTPStatus.NO_CONTENT,
            "schema": response_schema,
            "description": "`HTTP No Content [204]` indicating a successful update of bans",
        },
        "alt_responses": [{"status": HTTPStatus.REQUEST_ENTITY_TOO_LARGE}],
        "arguments": [
            {
                "location": "files",
                "schema": file_input_schema,
                "description": "List of users bans in JSON format.",
            }
        ],
    },
    # ----------------------------------------
    "/bans/perun-idm": {
        "methods": ["PUT"],
        "desc": """
Generalized endpoint behaving in the same way as the `/bans` endpoint. The only difference is
that the input data is passed in binary form as `.tar` file in the request.
""",
        "sum": "update_banned_users_generic",
        "response": {
            "status": HTTPStatus.NO_CONTENT,
            "schema": response_schema,
            "description": "`HTTP No Content` - indicating successful banning",
        },
        "alt_responses": [
            {
                "status": HTTPStatus.REQUEST_ENTITY_TOO_LARGE,
                "schema": response_schema,
                "description": "`HTTP Request Entity too large` - if the data passed to the request was larger than the upper limit",
            },
            {
                "status": HTTPStatus.UNPROCESSABLE_ENTITY,
                "schema": response_schema,
                "description": """`HTTP Unprocessable Entity` - if the banned users data couldn't be
                    parsed correctly or wasn't provided in the request at all""",
            },
        ],
        "arguments": [
            {
                "location": "files",
                "schema": file_input_schema,
                "description": "List of users to ban in `.tar` format in request data.",
            }
        ],
    },
    # ----------------------------------------
    "/bans/<string:ban_id>": {
        "methods": ["GET"],
        "desc": "Used for checking whether a ban with given `ban_id` exists. ",
        "sum": "find_ban",
        "response": {
            "status": HTTPStatus.OK,
            "example": {"_text": "Found ban dictionary"},
            "schema": string_schema,
            "description": """`HTTP OK [200]` indicating a successful operation, the body of the response includes either the ban information as a
  JSON if it exists or an empty JSON `{}` if a ban with given ID doesn't exist""",
        },
        "arguments": [
            {
                "location": "path",
                "schema": ban_id_argument_schema,
            }
        ],
    },
}
