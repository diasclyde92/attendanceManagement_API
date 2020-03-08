import datetime
from app.main.model.users import Users
from app.main.model.attendance_records import AttendanceRecords
import uuid
from app.main.service.constants import *
from bson.objectid import ObjectId
from flask_jwt_extended import create_access_token


def insert_attendance_records(data):
    # print(data)
    try:

        data_set = Users.objects.aggregate(
            *[{"$match": {"publicId": uuid.UUID(data['publicId'])}}, {"$project": {"id": 1}}])
        details = list(data_set)
        #print(details)

        # print(details[0])
        data['publicId'] = uuid.uuid4()
        data['userId'] = details[0]['_id']
        # print(data)

        if data['punchType'] == 'PUNCH_IN':
            del data['punchType']
            data['punchIn'] = datetime.datetime.utcnow()
            AttendanceRecords(**data).save()
        elif data['punchType'] == 'PUNCH_OUT':
            del data['punchType']
            data_set1 = AttendanceRecords.objects.aggregate(
                [
                    {"$match": {"userId": ObjectId(details[0]['_id'])}},
                    {"$sort": {"punchIn": -1}},
                    {"$project": {"publicId": 1}}
                ])
            update_id = list(data_set1)[0]['publicId']
            print(update_id)
            data['punchOut'] = datetime.datetime.utcnow()
            AttendanceRecords.objects(publicId=update_id).update(**data)

        else:
            return "Fail"

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
    print(data)
    data_set = Users.objects.aggregate(
        *[{"$match": {"publicId": uuid.UUID(data['publicId'])}}, {"$project": {"id": 1}}])
    details = list(data_set)
    user_id = details[0]
    print(user_id['_id'])

    data_set = AttendanceRecords.objects.aggregate(
        *[{"$match": {"userId": ObjectId(user_id['_id'])}}, {"$project": {"punchIn": 1, "punchOut": 1}}])
    details = list(data_set)
    print(details)
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


