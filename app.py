from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

import env
from data.db_models import db, Group, Location, Student
from data.validation_schemes import GroupSchema

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/groups", methods=["POST", "GET"])
def groups():
    """Create a new group, or get all groups"""
    if request.method == "POST":
        try:
            data = GroupSchema().load(request.json)

            new_group = Group(
                location_id=data.get("location_id"),
                name=data.get("name")
            )

            db.session.add(new_group)
            db.session.commit()

            return jsonify(new_group), 201

        except ValidationError as err:
            return jsonify(err.messages), 400

        except SQLAlchemyError as err:
            print(err.__dict__['orig'])
            return "Could not create group, please try again later.", 400

    else:
        all_groups = Group.query.all()
        return jsonify(all_groups), 200


@app.route("/groups/<uuid:group_id>")
def group(group_id):
    """Returns a specific group"""
    specific_group = Group.query.get(group_id)
    if specific_group:
        return jsonify(specific_group), 200
    return f"A group with id \"{group_id}\" doesn't exist.", 404


@app.route("/locations")
def locations():
    """Returns all locations"""
    all_locations = Location.query.all()
    return jsonify(all_locations), 200


@app.route("/locations/<uuid:location_id>")
def location(location_id):
    """Returns a specific location"""
    specific_location = Location.query.get(location_id)
    if specific_location:
        return jsonify(specific_location), 200
    return f"A location with id \"{location_id}\" doesn't exist.", 404


@app.route("/students")
def students():
    """Returns all students"""
    all_students = Student.query.all()
    return jsonify(all_students), 200


if __name__ == "__main__":
    app.run()
