from flask import Flask, request, jsonify
from sqlalchemy.exc import SQLAlchemyError
from marshmallow import ValidationError

import env
from data.db_models import db, Group
from data.validation_schemes import GroupSchema

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/group", methods=["POST"])
def create_group():
    """Create a new group"""
    request_data = request.json
    schema = GroupSchema()
    try:
        result = schema.load(request_data)

        group = Group(
            location_id=result.get("location_id"),
            name=result.get("name")
        )

        db.session.add(group)
        db.session.commit()

        return jsonify(group), 200

    except ValidationError as err:
        return jsonify(err.messages), 400

    except SQLAlchemyError as err:
        print(err.__dict__['orig'])
        return "Could not create group, please try again.", 400


if __name__ == "__main__":
    print("test")
    app.run()
