from flask_restplus import Api
from flask import Blueprint
from .main.controller.users_controller import api as users_ns
from .main.controller.attendance_records_controller import api as attendance_records_ns


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')

api = Api(blueprint,
          title='Attendance Management System',
          version='1.0',
          description='API web service'
          )


api.add_namespace(users_ns)
api.add_namespace(attendance_records_ns)