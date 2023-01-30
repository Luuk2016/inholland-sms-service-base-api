import os
from flask import Flask
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics

from api import api_bp
from data.db_models import db

# create the app
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DB_CONNECTION_STRING')

metrics = PrometheusMetrics(app)
metrics.info("app_info", "InHolland SMS Service Base API", version="1.0.0")

# setup CORS
CORS(
    app,
    resources={
        r"/*": {
            "origins": ["*"]
        }
    },
    supports_credentials=True
)

# initialize the app with the extension
db.init_app(app)

# for development only, remove for production
with app.app_context():
    db.create_all()

app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run()
