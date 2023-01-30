from flask_marshmallow import Marshmallow

ma = Marshmallow()


class LecturerSchema(ma.Schema):
    """Schema for lecturer"""

    class Meta:  # pylint: disable=R0903
        """Lecturer schema meta"""
        fields = ("id", "email")


lecturer_schema = LecturerSchema()
lecturers_schema = LecturerSchema(many=True)
