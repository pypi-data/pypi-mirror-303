import yaml
from flask_smorest import Api
from deepdiff import DeepDiff


def api_setup(app, openapi_version):
    API_SPEC_OPTIONS = {
        "components": {
            "securitySchemes": {
                "NegotiateAuth": {
                    "type": "http",
                    "scheme": "negotiate",
                },
                "oAuthScheme": {
                    "type": "oauth2",
                    "description": "This API/Endpoint uses OAuth 2.",
                    "flows": {
                        "implicit": {
                            "authorizationUrl": "authorizationUrl",
                            "scopes": {},
                        }
                    },
                },
                "bearerAuthJWT": {
                    "type": "http",
                    "scheme": "bearer",
                    "bearerFormat": "JWT",
                },
            }
        },
    }
    default_version = "1.0.0"

    # Api setup
    app.config["API_TITLE"] = "Proxygui API"
    app.config["API_VERSION"] = (
        default_version if openapi_version is None else openapi_version
    )
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["API_SPEC_OPTIONS"] = API_SPEC_OPTIONS

    api = Api(app)

    return app, api


# Parse paths, endpoints and security schemas from API for future comparison
def parse_api(in_dict):
    paths = in_dict["paths"]

    # Endpoints -----------------
    endpoint_nested = [
        [key + ":" + subkey for subkey in paths[key] if subkey != "parameters"]
        for key in paths.keys()
    ]
    endpoints = [x for xs in endpoint_nested for x in xs]

    # Security ------------------
    securitySchema = in_dict.get("components", {}).get("securitySchemes", {})
    security_types = [
        (key, securitySchema.get(key, {}).get("type"))
        for key in sorted([k for k in securitySchema.keys()])
    ]

    return paths, endpoints, security_types


# Retrive names of enpoints and names of required parameters
def get_required_params(paths):
    keys = sorted([k for k in paths.keys()])
    paths_params = [paths[k].get("parameters", []) for k in keys]

    name_params = []

    # Saving both endpoint and parameter for case of parameter name similarity
    for key, param in zip(keys, paths_params):
        name_params.append({"endpoint": key, "params": param})

    required_params = []

    for endpoint in name_params:
        params = endpoint.get("params", [])
        if params == []:
            continue

        for param in params:
            if "required" in param.keys():
                required_params.append(
                    endpoint.get("endpoint") + ":" + param.get("name")
                )
    return required_params


# Retrieve list of parameters for each path
def get_params(paths) -> dict:
    return [(paths[k].get("parameters", [])) for k in sorted([k for k in paths.keys()])]


# Checking parameters in request - change or removal
def compare_request_params(old_paths, new_paths) -> bool:
    old_params = get_params(old_paths)
    new_params = get_params(new_paths)

    # Checking for removed params in each endpoint
    for old, new in zip(old_params, new_params):
        if old == new:  # Same parameters
            return True
        for param in old:
            print(param)
            if param not in new:
                return False

            old_schema = param.get("schema", {})
            new_schema = next(
                (item for item in new if item["name"] == param.get("name", "")),
                None,
            ).get("schema", {})
            if DeepDiff(old_schema, new_schema) != {}:
                return False
    return True


# Check if api contains breaking change
# True - contains Breaking change, False - it does not
def check_breaking_change(old_api, new_api):
    old_paths, old_ep, old_sec = parse_api(old_api)
    new_paths, new_ep, new_sec = parse_api(new_api)

    # Fast compare endpoints for removed ones
    if list(set(old_ep) - set(new_ep)) != []:
        return True

    # Check for change in required parameters
    if not get_required_params(old_paths) == get_required_params(new_paths):
        return True

    # remove or change the type of a request parameter or response attribute
    if not compare_request_params(old_paths, new_paths):
        return True

    # Check for substantial changes in security schemas
    if not old_sec == new_sec:
        return True

    return False


def load_yaml_to_api(cfg):
    filename = cfg.get("open_api", {}).get("filename", None) + ".yaml"
    try:
        with open(filename, "r") as stream:
            file = yaml.safe_load(stream)
    except Exception:
        file = None

    return file


def compare_versions(cfg, api=None):
    old_api = load_yaml_to_api(cfg)  # Previous Api loaded from openapi.yaml file
    if old_api is None:  # Default, when no previous were loaded
        return "1.0.0"

    old_ver = old_api["info"]["version"]
    if api is None:
        # No need to increase OpenAPI version while developing
        return old_ver

    new_api = api.spec.to_dict()  # Newly asssembled Api from current App

    # ------------------
    old_ver = [int(x) for x in old_ver.split(".")]

    # Getting difference between dicts / YAML files
    diff_obj = DeepDiff(old_api, new_api)
    diff = diff_obj.get("values_changed", {})
    # Major -> +1.0.0
    if check_breaking_change(old_api, new_api):
        print("Major difference - Breaking change in Api")
        old_ver[0] += 1
        old_ver[1] = 0
        old_ver[2] = 0
    else:
        # Remove version, because new Api has default version that
        # is not reflecting actual api
        if diff.get("root['info']['version']", None) is not None:
            diff.pop("root['info']['version']")
        # Minor -> X.+1.0
        if diff != {}:
            print("Minor differece in Api")
            old_ver[1] += 1
            old_ver[2] = 0
        # Patch -> X.X.+1
        else:
            print("Patch difference in Api")
            old_ver[2] += 1
    return ".".join([str(x) for x in old_ver])
