from flask import Flask, jsonify
import env
from data.models import db, Location

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/location")
def get_locations():
    """Returns all locations"""
    locations = Location.query.all()
    return jsonify(locations)


if __name__ == "__main__":
    print("test")
    app.run()
