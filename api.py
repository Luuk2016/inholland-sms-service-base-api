import uuid
from flask import request, jsonify, Blueprint
from sqlalchemy import asc
from sqlalchemy.exc import IntegrityError, SQLAlchemyError
from marshmallow import ValidationError

from data.db_models import db, Group, Location, Student, Lecturer
from data.db_schemas import lecturers_schema
from data.validation_schemes import GroupValidationSchema, StudentValidationSchema,\
    AuthValidationSchema

api_bp = Blueprint('api', __name__, url_prefix='/')


@api_bp.route("/groups")
def get_groups():
    """Get all groups"""
    try:
        all_groups = Group.query.all()

        if len(all_groups) == 0:
            return "No groups could be found", 200

        return jsonify(all_groups), 200

    except SQLAlchemyError:
        return "Groups couldn't be retrieved", 400


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
    try:
        specific_group = Group.query.get(group_id)

        if not specific_group:
            return f"A group with id \"{group_id}\" doesn't exist.", 404

        return jsonify(specific_group), 200

    except SQLAlchemyError:
        return "Group couldn't be retrieved", 400


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
    try:
        students = Student.query \
            .join(Group, Student.group_id == group_id) \
            .filter(Student.group_id == group_id) \
            .order_by(asc(Student.name)) \
            .all()

        if len(students) == 0:
            return "No students could be found", 200

        return jsonify(students), 200

    except SQLAlchemyError:
        return "Students couldn't be retrieved", 400


@api_bp.route("/locations")
def get_locations():
    """Returns all locations"""
    try:
        all_locations = Location.query.all()

        if len(all_locations) == 0:
            return "No locations could be found", 200

        return jsonify(all_locations), 200

    except SQLAlchemyError:
        return "Locations couldn't be retrieved", 400


@api_bp.route("/locations/<uuid:location_id>")
def get_location(location_id):
    """Returns a specific location"""
    try:
        specific_location = Location.query.get(location_id)

        if not specific_location:
            return f"A location with id \"{location_id}\" doesn't exist.", 404

        return jsonify(specific_location), 200

    except SQLAlchemyError:
        return "Location couldn't be retrieved", 400


@api_bp.route("/lecturer", methods=["GET"])
def get_lecturers():
    """Get all lecturers"""
    all_lecturers = Lecturer.query.all()
    output = lecturers_schema.dump(all_lecturers)
    return jsonify(output), 200


@api_bp.route("/lecturer", methods=["POST"])
def create_lecturer():
    """Create lecturer (account)"""
    try:
        data = AuthValidationSchema().load(request.json)

        lecturer = Lecturer(
            email=data.get("email"),
            password=data.get("password")
        )

        db.session.add(lecturer)
        db.session.commit()

        return jsonify(lecturer), 201

    except ValidationError as err:
        return jsonify(err.messages), 400

    except IntegrityError as err:
        db.session.rollback()
        if "key value violates unique constraint \"lecturer_email_key\"" in err.args[0]:
            return "Email address is already in use", 400

    return "Could not create lecturer, please try again later", 400


@api_bp.route("/login", methods=["POST"])
def login():
    """Log in as lecturer with credentials"""
    try:
        data = AuthValidationSchema().load(request.json)

        lecturer = Lecturer.query.filter_by(
            email=data.get('email')
        ).first()

        if lecturer and lecturer.check_password(data.get('password')):
            token = lecturer.encode_token()

            return jsonify({
                "auth_token": 'Bearer ' + token,
                "lecturer": {
                    "id": lecturer.id,
                    "email": lecturer.email
                }
            }), 200

        return "Lecturer could not be found", 404
    except ValidationError as err:
        return jsonify(err.messages), 400
    except TypeError:
        return jsonify("The JWT token is invalid"), 401


@api_bp.route("login-verify", methods=["POST"])
def login_verify():
    """Log in as lecturer with JWT token"""
    auth_header = request.headers.get("Authorization")

    if auth_header:
        token = auth_header.split(" ")[1]
        lecturer_id = Lecturer.decode_token(token)

        try:
            lecturer = Lecturer.query.filter_by(id=uuid.UUID(lecturer_id)).first()
            return jsonify({
                "id": lecturer.id,
                "email": lecturer.email
            }), 200
        except ValueError:
            return jsonify("Token subject is an invalid uuid"), 401
    else:
        return jsonify("Provide a valid auth token"), 401
