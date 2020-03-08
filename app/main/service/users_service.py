

from app.main.model.users import Users
import uuid
from app.main.service.constants import *
from flask_jwt_extended import create_access_token


def insert_users(data):
    try:
        if not Users.objects(username=data['username'].upper()):
            data['publicId'] = uuid.uuid4()
            data['username'] = data['username'].upper()
            salt = gen_salt()
            data['password'] = hash_password('optel', salt)
            data['passwordSalt'] = salt
            Users(**data).save()
            response_object = {
                'status': Const.SUCCESS,
                'message': 'User created successfully.'
            }
            return response_object, Const.SUCCESS_CODE
        else:
            response_object = {
                'status': Const.FAIL,
                'message': 'Username already exists.'
            }
            return response_object
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def update_users(data):
    try:
        Users.objects(publicId=data['publicId']).update(**data)
        response_object = {
            'status': Const.SUCCESS,
            'message': 'User updated successfully.'
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def fetch_users(data):
    project_data = {"$project": {
                'publicId': 1,
                'username': 1,
                'name': 1,
                'email': 1,
                'status': 1,
                'userType': 1
                }
            }
    if data['publicId'] is not None:
        try:
            data_set = Users.objects.aggregate(*[
                {"$match": {"publicId": uuid.UUID(data['publicId'])}},
                project_data
            ])
            details = list(data_set)
            return details
        except Exception as e:
            response_object = {
                'status': Const.FAIL,
                'message': e
            }
            return response_object

    query_data = []
    if data['page'] is not None:
        query_data.append({"$limit": (int(int(data['page']) * int(data['per_page'])))})
        query_data.append({"$skip": (int(int(data['page'] - 1) * int(data['per_page'])))})
    else:
        query_data.append({"$limit": (int(10))})
        query_data.append({"$skip": (int(0))})

    query_data.append(project_data)
    data_set = Users.objects.aggregate(*query_data)
    details = list(data_set)
    return details


def delete_users(data):
    try:
        Users.objects(publicId=data['publicId']).delete()
        response_object = {
            'status': Const.SUCCESS,
            'message': 'User deleted successfully.'
        }
        return response_object, Const.SUCCESS_CODE
    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def generate_active_token(public_id, role):
    try:
        identity = {
            'publicId': public_id,
            'role': role
        }
        access_token = create_access_token(expires_delta=False, identity=identity)
        return access_token
    except Exception as e:
        return e


def login_user(data):
    for item in Users.objects(username=data['username'].upper()):
        verify = verify_password(data['password'], item['password'].encode('utf-8'), item['passwordSalt'])
        if not verify:
            response_object = {
                'status': Const.FAIL,
                'message': 'Incorrect username or password.'
            }
            return response_object
        token = generate_active_token(item['publicId'], item['userType'])
        response_object = {
            'status': Const.SUCCESS,
            'token': token,
            'publicId': str(item['publicId']),
            'message': 'Authentication Success.'
        }
        return response_object
    response_object = {
        'status': Const.FAIL,
        'message': 'Incorrect username or password.'
    }
    return response_object

