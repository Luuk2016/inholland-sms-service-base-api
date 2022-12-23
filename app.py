from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import env

# create the extension
db = SQLAlchemy()
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = env.CONNECTION_STRING
# initialize the app with the extension
db.init_app(app)


@app.route("/")
def hello_world():
    """Return a basic message"""
    return "<p>Hello, World!</p>"
