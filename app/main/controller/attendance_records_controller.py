
from ..service.attendance_records_service import insert_attendance_records, fetch_attendance_records, \
                                                 update_attendance_records, delete_attendance_records
from app.main.util.roles.roles import roles_required
from ..util.attendance_records_dto import AttendanceRecordsDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask_restplus import reqparse
from flask import request


parser = reqparse.RequestParser()
parser.add_argument('page', type=int, required=False)
parser.add_argument('per_page', type=int, required=False, choices=[5, 10, 20, 30, 40, 50])
parser.add_argument('publicId', type=str, required=False)

api = AttendanceRecordsDto.api

_insert_attendance_records = AttendanceRecordsDto.AttendanceRecordsPost
_fetch_attendance_records = AttendanceRecordsDto.AttendanceRecordsGet
_update_attendance_records = AttendanceRecordsDto.AttendanceRecordsPut
_delete_attendance_records = AttendanceRecordsDto.AttendanceRecordsDelete


@api.route('/')
class AttendanceRecords(Resource):
    @api.expect(_insert_attendance_records, validate=True)
    # @api.doc(security='apikey')
    # @roles_required('ADMIN')
    def post(self):
        """Create a new Attendance record"""
        data = request.json
        return insert_attendance_records(data=data)

    # @api.doc(security='apikey')
    # @roles_required('ADMIN')
    @api.expect(_update_attendance_records, validate=True)
    def put(self):
        """Update Attendance record"""
        data = request.json
        return update_attendance_records(data=data)

    # @api.doc(security='apikey')
    # @roles_required('ADMIN')
    @api.expect(parser, validate=True)
    @api.marshal_list_with(_fetch_attendance_records, envelope='data')
    def get(self):
        """List Attendance records"""
        args = parser.parse_args()
        return fetch_attendance_records(data=args)

    # @api.doc(security='apikey')
    # @roles_required('ADMIN')
    @api.expect(_delete_attendance_records, validate=True)
    def delete(self):
        """Delete User"""
        data = request.json
        return delete_attendance_records(data=data)

