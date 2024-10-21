from marshmallow import fields, Schema
from flask_smorest.fields import Upload


# -------------------------- Input schemas ----------------------------------
# /bans
# /bans/perun-idm
class file_input_schema(Schema):
    data = Upload()


# /bans/<string:ban_id>
class ban_id_argument_schema(Schema):
    ban_id = fields.String(
        metadata={"description": "ID of a potential ban in the URL parameter"}
    )


# /backchannel-logout
class backchannel_oidc_schema(Schema):
    form = fields.String(
        metadata={
            "description": "[OIDC Logout Token](https://openid.net/specs/openid-connect-backchannel-1_0.html#LogoutToken)"
        }
    )


# /verify/<string:consent_id>
# /users/me/consents/<string:consent_id>
class consent_id_argument_schema(Schema):
    consent_id = fields.String(metadata={"description": "Consent ID description"})


# /creq/<string:jwt>
class jwt_arguments_schema(Schema):
    jwt = fields.String(metadata={"description": "JWT token"})
