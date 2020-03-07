from flask_jwt_extended import decode_token
from functools import wraps
from flask import request


def roles_required(*role_names):
    def wrapper(view_function):
        @wraps(view_function)
        def decorator(*args, **kwargs):
            token = None
            if 'X-API-KEY' in request.headers:
                token = request.headers['X-API-KEY']
            if not token:
                return {'message': 'Token is missing.'}, 401
            try:
                info = decode_token(token)
                role = info['identity']['role']
                if role not in role_names:
                    return {'message': 'Invalid user'}, 401
            except Exception as e:
                return {'message': 'Invalid Token.'}, 401
            return view_function(*args, **kwargs)
        return decorator
    return wrapper
