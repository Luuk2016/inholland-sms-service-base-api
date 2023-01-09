from flask_marshmallow import Marshmallow
from marshmallow import fields

ma = Marshmallow()


class LecturerSchema(ma.Schema):
    class Meta:
        fields = ("id", "email")


lecturer_schema = LecturerSchema()
lecturers_schema = LecturerSchema(many=True)
