from flask import Flask
from api import api_bp
from data.db_models import db
import os

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('CONNECTION_STRING')

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()

app.register_blueprint(api_bp)


if __name__ == "__main__":
    app.run()
