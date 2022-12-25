from flask import Flask
import env
from data.models import db

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()


@app.route("/")
def hello_world():
    """Return a basic message"""
    return "<p>Hello, World!</p>"


if __name__ == "__main__":
    print("test")
    app.run()
