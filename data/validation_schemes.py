from marshmallow import Schema, fields, validate


class GroupValidationSchema(Schema):
    """Used to validate the posted data when trying to create a new group"""
    location_id = fields.UUID(required=True)
    # noinspection PyTypeChecker
    name = fields.Str(required=True, validate=validate.Length(min=2))


class StudentValidationSchema(Schema):
    """Used to validate the posted data when trying to create a new student"""
    # noinspection PyTypeChecker
    name = fields.Str(required=True, validate=validate.Length(min=2))
    # noinspection PyTypeChecker
    phone_number = fields.Str(required=True, validate=validate.Length(min=2))
