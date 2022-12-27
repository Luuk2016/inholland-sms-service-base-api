from marshmallow import Schema, fields, validate


class GroupSchema(Schema):
    """Used to validate the posted data when trying to create a new group"""
    location_id = fields.UUID(required=True)
    # noinspection PyTypeChecker
    name = fields.Str(required=True, validate=validate.Length(min=2, error="Field cannot be blank"))
