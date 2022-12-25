from marshmallow import Schema, fields


class GroupSchema(Schema):
    """Used to validate the posted data when trying to create a new group"""
    location_id = fields.UUID(required=True)
    name = fields.String(required=True)
