from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from marshmallow import ValidationError

import env
from data.db_models import db, Group, Location
from data.validation_schemes import GroupSchema

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/groups")
def get_groups():
    """Get all groups"""
    all_groups = Group.query.all()
    return jsonify(all_groups), 200


@app.route("/groups", methods=["POST"])
def create_group():
    """Create a new group"""
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

    except IntegrityError as err:
        db.session.rollback()
        if "violates unique constraint \"group_name_key\"" in err.args[0]:
            return "Group name already exists", 400
        if "is not present in table \"location\"" in err.args[0]:
            return "No location with that id exists", 400

    return "Could not create group, please try again later.", 400


@app.route("/groups/<uuid:group_id>")
def get_group(group_id):
    """Returns a specific group"""
    specific_group = Group.query.get(group_id)
    if specific_group:
        return jsonify(specific_group), 200
    return f"A group with id \"{group_id}\" doesn't exist.", 404


@app.route("/locations")
def get_locations():
    """Returns all locations"""
    all_locations = Location.query.all()
    return jsonify(all_locations), 200


@app.route("/locations/<uuid:location_id>")
def get_location(location_id):
    """Returns a specific location"""
    specific_location = Location.query.get(location_id)
    if specific_location:
        return jsonify(specific_location), 200
    return f"A location with id \"{location_id}\" doesn't exist.", 404


if __name__ == "__main__":
    app.run()
