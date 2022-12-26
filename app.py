from flask import Flask, jsonify
import env
from data.models import db, Group, Location

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/group/<uuid:group_id>")
def group(group_id):
    """Returns a specific group"""
    specific_group = db.get_or_404(Group, group_id)
    return jsonify(specific_group)


@app.route("/group")
def groups():
    """Returns all groups"""
    all_groups = Group.query.all()
    return jsonify(all_groups)


@app.route("/location")
def locations():
    """Returns all locations"""
    all_locations = Location.query.all()
    return jsonify(all_locations)


if __name__ == "__main__":
    print("test")
    app.run()
