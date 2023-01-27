from flask import request
from functools import wraps
from data.db_models import Lecturer


def auth_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        token = auth_header.split(" ")[1]

        if not auth_header:
            return "Not authenticated", 401
        try:
            lecturer_id = Lecturer.decode_token(token)
            lecturer = Lecturer.query.filter_by(id=lecturer_id).first()

            if not lecturer:
                return "Lecturer was not found", 404
        except ValueError:
            return "Token content is invalid", 401
        return f(*args, **kwargs)

    return decorator
