# perun.proxygui

Pages used by microservices
in [satosacontrib.perun](https://gitlab.ics.muni.cz/perun/perun-proxyidp/satosacontrib-perun).

## Installation

The recommended way to install is via pip:

```sh
pip3 install perun.proxygui
```

Alternatively, you can clone the repository and run:

```sh
pip3 install .
```

You also need to install the appropriate sqlalchemy driver. For PostgreSQL, you can include the `postgresql` extra, which will install [psycopg2-binary](https://pypi.org/project/psycopg2-binary/):

```sh
pip3 install perun.proxygui[postgresql]
```

## Configuration

### General

Copy `perun.proxygui.yaml` from config_templates to `/etc/` (it needs to reside at `/etc/perun.proxygui.yaml`) and
adjust to your needs.

The `global_cfg_filepath` option needs to point to the location of the global microservice config from
the [satosacontrib.perun](https://gitlab.ics.muni.cz/perun/perun-proxyidp/satosacontrib-perun) module. You also need
to set the attribute map config.

At the very least, you need to copy the config templates:

```sh
cp config_templates/perun.proxygui.yaml /etc/perun.proxygui.yaml
cp ../satosacontrib-perun/satosacontrib/perun/config_templates/attribute_typing.yaml /etc/
cp ../satosacontrib-perun/satosacontrib/perun/config_templates/microservices_global.yaml /etc/
```

Then change the following line in `/etc/perun.proxygui.yaml`:

```yaml
global_cfg_filepath: /etc/microservices_global.yaml
```

And the following line in `/etc/microservices_global.yaml`:

```yaml
attrs_cfg_path: /etc/attribute_typing.yaml
```

### Backchannel logout

Analogous to general configuration. Copy `backchannel-logout.yaml` from config_templates to `/etc/` so the resulting
filepath is `/etc/backchannel-logout.yaml` and adjust to your needs.

This configuration is necessary for using `/backchannel-logout` endpoint. It
performs [OIDC Back-Channel Logout 1.0](https://openid.net/specs/openid-connect-backchannel-1_0.html) using
the [idpy-oidc](https://github.com/IdentityPython/idpy-oidc) library.

OIDC builds upon OAuth 2.0. Config options `issuer`, `client_id` and `client_secret` are terms explained
in [OAuth 2.0 [RFC6749]](https://datatracker.ietf.org/doc/html/rfc6749#section-2.2).

The endpoint accepts
an [OIDC Logout Token](https://openid.net/specs/openid-connect-backchannel-1_0.html#LogoutToken)
which is a JWT with the necessary information for performing back-channel logout. Therefore, the `key_conf` setting must
contain paths to the key pair configured between an OP (our endpoint) which decrypts the JWT and an RP (endpoint caller)
who encrypts the JWT. Options `private_path` and `public_path` represent filepaths to the private/public key.
Settings `key_defs` specify key types and `read_only` determines whether the keys are read-only. Both come from the
[idpy-oidc](https://github.com/IdentityPython/idpy-oidc) library.

## Run

### uWSGI

To run this Flask app with uWSGI, use the callable perun.proxygui.app:get_app, e.g.

```plain
module = perun.proxygui.app:get_app
```

### local development

```sh
python3 perun/proxygui/app.py
```

Now the app is available at `http://localhost:5000/` (e.g. `http://localhost:5000/bans`).

### local OpenAPI development

To create local, temporal OpenAPI scheme from current version run following command:

```sh
flask --app perun.proxygui.app:get_openapi openapi write --format=yaml "temp_out_file.yaml"
```

## Translations

### Babel

First you need to generate `.pot` file: `pybabel extract -F babel.cfg -o messages.pot .`

Next step is to generate `.po` file: `pybabel init -i messages.pot -d perun/proxygui/gui/translations -D messages -l <language_code>`

- replace `<language code>` with given language code (eg: fr)

Then you need to, manually or using a tool like [Poedit](https://poedit.net/), write your translations in the generated `.po` file and compile it: `pybabel compile -d perun/proxygui/gui/translations -D messages`

- note that if the `.pot` file is already created and you want to add new language ignore the first step

## API

### Main part of documentation

In `openapi.yaml` is OpenAPI specification openable in editors (e.g. [Swagger Editor](https://editor.swagger.io/))

### Heuristic page

Provides information about user authentication events gathered by the AuthEventLogging microservice, to confirm their identity e.g. during a MFA reset.

**Endpoint:** `/heuristics`

**Description:** Used to gather ID of searched user

**Result:**

- `HTTP OK [200]` indicating successfull load of search page

**Endpoint:** `/heuristics/<user_id>`

**Method:** `GET`

**Description:** Used for showing gathered information about past authentications of user, and showing statistics based on that data.

**Performed MFA:** Gathered logs are checked if MFA was performed while handling the original logging event. Upstream ACRs values are compared to two hardcoded values: `https://refeds.org/profile/mfa` and `http://schemas.microsoft.com/claims/multipleauthn`. Database log for local MFA are checked apart from the upstream ACRs.

**Input arguments:** ID of searched user

**Result:**

- `HTTP OK [200]` indicating successfull load of show page

## Future development notes

Currently, all blueprints need to be prefixed with `url_prefix="/proxygui"`. To load static files, use
`url_for(".static", filename="example.js")` command.

## Adding new endpoint to blueprint and OpenAPI specs

Standart way to add new endpoint is to put decorator `@target_blueptrint.route(...)` before target function.

When adding endpoint to OpenAPI that decorator had to be replaced with `@openapi_route(route, blueprint)` imported from `perun.proxygui.openapi.openapi_data`. Next step is to create additional entry in `data` dictionary, also in that file. That entry has a format of nested dictionary. Example:

```json
"/example_endpoint":{       # Key is route to the endpoint
    "desc": "Endpoint description",             # OPRIONAL, Full description of endpoit
    "sum": "Endpoint summary",                  # OPRIONAL, Brief description of endpoint
                                                #   (e.g. name, purpose, ...)
    "security": [{"NegotiateAuth": []}],        # OPTIONAL, scheme choosed from dictionary
                                                #   defined in `openapi.py`
    "response": {
      "status": HTTPStatus.OK,                  # OPTIONAL
      "schema": redirect_response               # OPTIONAL class name of describing scheme, described below
      "example": {"_text": "Example resonse"}   # Example that is compatible with schema
    },
    "arguments": [                              # OPTIONAL list of endpoints arguments
      {
        "location": "path",                     # Example of argument in path
        "schema": schema class
      },
      {
        "location": "files",                    # Example of request argument
        "schema": file_upload_schema,
        "description": "argument description"
      },
      ...
    ],
    "alt_responses": [                          # OPTIONAL
      {
        # List of response dictionaries
      }
    ]
},
```

### schema

schema of endpoint response, in runtime response is check against this sheme (if it is defined, if not, response is not checked at all), when not matched typically respond contains only empty dict. If it is defined, it has two variants (similar scheme is used to define arguments):

- **JSON / jsoify** - create simple class from marshmallow `Schema` class, with attributes that are

same as returned JSON from endpoint (basically that class wraps those attributes as JSON dictionary)
Example:

```python
class delete_consent_schema(marshmallow.Schema):
    deleted = fields.Boolean()
    message = fields.String()
```

- **Response / redirect / abort** - in case of these responses, scheme in response decorator can be custom (it is ignored when creating endpoint response)

- **String** - redo to JSON with already created schema `string_schema` with only atribute `_text`. Then in response handling add additional `json.loads()` wrapping function

```python
return jsonify({"_text": "Original String text"})
```
