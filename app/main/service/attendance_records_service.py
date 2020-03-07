import datetime
from app.main.model.users import Users
from app.main.model.attendance_records import AttendanceRecords
import uuid
from app.main.service.constants import *
from flask_jwt_extended import create_access_token


def insert_attendance_records(data):
    # print(data)
    try:

        data_set = Users.objects.aggregate(
            *[{"$match": {"publicId": uuid.UUID(data['publicId'])}}, {"$project": {"id": 1}}])
        details = list(data_set)
        # print(details[0])
        data['publicId'] = uuid.uuid4()
        data['userId'] = details[0]['_id']
        # print(data)

        if data['punchType'] == 'PUNCH_IN':
            del data['punchType']
            data['punchIn'] = datetime.datetime.utcnow()
        elif data['punchType'] == 'PUNCH_OUT':
            del data['punchType']
            data['punchOut'] = datetime.datetime.utcnow()
        else:
            return "Fail"
        AttendanceRecords(**data).save()
        print(data)

        # data['username'] = data['username'].upper()
        # salt = gen_salt()
        # data['password'] = hash_password('optel', salt)
        # data['passwordSalt'] = salt
        # Users(**data).save()
        response_object = {
            'status': Const.SUCCESS,
            'message': 'User created successfully.'
        }
        return response_object, Const.SUCCESS_CODE

    except Exception as e:
        response_object = {
            'status': Const.FAIL,
            'message': e
        }
        return response_object, Const.FAILURE_CODE


def update_attendance_records(data):
    return "Success"


def fetch_attendance_records(data):
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


def delete_attendance_records(data):
    try:
        AttendanceRecords.objects(publicId=data['publicId']).delete()
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


