from marshmallow import fields, Schema

# ------------------------- Response schemas --------------------------------
# ---------------------------------------------------------------------------
# String/JSON - actualy used when procesing a response


# /verify/<string:consent_id>
class consent_attrs_schema(Schema):
    # consent.attributes fields
    # TODO add exact fromat of consent attributes
    pass


# /bans/<string:ba_id>
class string_schema(Schema):
    _text = fields.String()


# /users/me/consents
class consent_schema(Schema):
    user_id = fields.String()
    requester = fields.String()
    attributes = fields.Dict()
    months_valid = fields.String()
    timestamp = fields.String()


class user_consents_schema(Schema):
    consents = fields.List(fields.Nested(consent_schema))


# /users/me/consents/<string:consent_id>
class delete_consent_schema(Schema):
    deleted = fields.Boolean()
    message = fields.String()


# -------------------------------------------------------------------------
# Schemas for Response type return value (Response, redirect, ...)
# only for API purpose


# /bans/perun-idm
# /bans
class response_schema(Schema):
    response = fields.String(load_default="flask.Response class is returned")


# /save_consent
class redirect_schema(Schema):
    response = fields.String(
        load_default="flask.Response class via redirect is returned"
    )
