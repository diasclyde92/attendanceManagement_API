from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class AttendanceRecordsDto:
    api = Namespace('attendance-records', authorizations=authorizations, description='Attendance records related '
                                                                                     'operations')

    AttendanceRecordsPost = api.model('AttendanceRecordsPost', {
        'publicId': fields.String(),
        'punchType': fields.String(),
        # 'punchIn': fields.DateTime(),
        # 'punchOut': fields.DateTime(),
        # 'userId': fields.String(),
        # 'adminUpdate': fields.Boolean(),
        # 'updatedBy': fields.String(),
        # 'updatedOn': fields.DateTime()
    })

    AttendanceRecordsPut = api.model('AttendanceRecordsPut', {
        'publicId': fields.String(),
        'username': fields.String(),
        'punchIn': fields.DateTime(),
        'punchOut': fields.DateTime(),
        'userId': fields.String(),
        'adminUpdate': fields.Boolean(),
        'updatedBy': fields.String(),
        'updatedOn': fields.DateTime()
    })

    AttendanceRecordsGet = api.model('AttendanceRecordsGet', {
        'publicId': fields.String(),
        'username': fields.String(),
        'punchIn': fields.DateTime(),
        'punchOut': fields.DateTime(),
        'userId': fields.String(),
        'adminUpdate': fields.Boolean(),
        'updatedBy': fields.String(),
        'updatedOn': fields.DateTime()
    })

    AttendanceRecordsDelete = api.model('AttendanceRecordsDelete', {
        'publicId': fields.String()
    })

