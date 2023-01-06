from flask import request, jsonify, Blueprint
from sqlalchemy import asc
from sqlalchemy.exc import IntegrityError
from marshmallow import ValidationError
from data.db_models import db, Group, Location, Student, Lecturer
from data.validation_schemes import GroupValidationSchema, StudentValidationSchema, AuthValidationSchema

api_bp = Blueprint('api', __name__, url_prefix='/')


@api_bp.route("/groups")
def get_groups():
    """Get all groups"""
    all_groups = Group.query.all()
    return jsonify(all_groups), 200


@api_bp.route("/groups", methods=["POST"])
def create_group():
    """Create a new group"""
    try:
        data = GroupValidationSchema().load(request.json)

        new_group = Group(
            location_id=data.get("location_id"),
            name=data.get("name")
        )

        db.session.add(new_group)
        db.session.commit()

        return jsonify(new_group), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except IntegrityError as err:
        db.session.rollback()
        if "violates unique constraint \"group_name_key\"" in err.args[0]:
            return "Group name already exists", 400
        if "is not present in table \"location\"" in err.args[0]:
            return "No location with that id exists", 400

    return "Could not create group, please try again later.", 400


@api_bp.route("/groups/<uuid:group_id>")
def get_group(group_id):
    """Returns a specific group"""
    specific_group = Group.query.get(group_id)
    if specific_group:
        return jsonify(specific_group), 200
    return f"A group with id \"{group_id}\" doesn't exist.", 404


@api_bp.route("/groups/<uuid:group_id>/students", methods=["POST"])
def add_student_to_group(group_id):
    """Add a student to a group"""
    try:
        data = StudentValidationSchema().load(request.json)

        new_student = Student(
            group_id=group_id,
            name=data.get("name"),
            phone_number=data.get("phone_number")
        )

        db.session.add(new_student)
        db.session.commit()

        return jsonify(new_student), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except IntegrityError as err:
        db.session.rollback()
        if "key value violates unique constraint \"student_phone_number_key\"" in err.args[0]:
            return "Phone number is already in use.", 400
        if "is not present in table \"group\"" in err.args[0]:
            return "No group with that id exists", 400

    return "Could not add student to group, please try again later.", 400


@api_bp.route("/groups/<uuid:group_id>/students")
def get_students_from_group(group_id):
    """Get all students from a specific group"""
    students = Student.query \
        .join(Group, Student.group_id == group_id) \
        .filter(Student.group_id == group_id) \
        .order_by(asc(Student.name)) \
        .all()

    return jsonify(students), 200


@api_bp.route("/locations")
def get_locations():
    """Returns all locations"""
    all_locations = Location.query.all()
    return jsonify(all_locations), 200


@api_bp.route("/locations/<uuid:location_id>")
def get_location(location_id):
    """Returns a specific location"""
    specific_location = Location.query.get(location_id)
    if specific_location:
        return jsonify(specific_location), 200
    return f"A location with id \"{location_id}\" doesn't exist.", 404


@api_bp.route("/lecturer", methods=["POST"])
def login():
    """Create lecturer/account"""
    try:
        data = AuthValidationSchema().load(request.json)

        new_lecturer = Lecturer(
            email=data.get("email"),
            password=data.get("password")
        )

        db.session.add(new_lecturer)
        db.session.commit()

        return jsonify(new_lecturer), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except IntegrityError as err:
        db.session.rollback()
        if "key value violates unique constraint \"lecturer_email_key\"" in err.args[0]:
            return "Email address is already in use", 400

    return "Could not create lecturer, please try again later", 400
