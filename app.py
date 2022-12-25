from flask import Flask, request, jsonify
from marshmallow import ValidationError

import env
from data.models import db
from data.schemes import GroupSchema

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
    """Return a basic message"""
    request_data = request.json
    schema = GroupSchema()
    try:
        result = schema.load(request_data)
    except ValidationError as err:
        return jsonify(err.messages), 400

    return jsonify(result), 200


if __name__ == "__main__":
    print("test")
    app.run()
