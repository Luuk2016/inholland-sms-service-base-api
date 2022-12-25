from flask import Flask, jsonify
import env
from data.models import db, Group

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/group/<uuid:group_id>")
def get_specific_group(group_id):
    """Returns a specific group"""
    group = db.get_or_404(Group, group_id)
    return jsonify(group)


if __name__ == "__main__":
    print("test")
    app.run()
