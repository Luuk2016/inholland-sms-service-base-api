from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a basic message"""
    return "<p>Hello, World!</p>"
