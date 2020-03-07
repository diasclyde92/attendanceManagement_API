"""
* Name: user_types_controller.py
* Description : All User types API's
* Author: www.opspl.com
* Date Created: 2nd Dec 2019
* Date Modified: 2nd Dec 2019
*
"""

from ..service.users_service import insert_users, fetch_users, update_users, delete_users, login_user

from app.main.util.roles.roles import roles_required
from ..util.users_dto import UsersDto
from app.main.service.constants import *
from flask_restplus import Resource
from flask_restplus import reqparse
from flask import request


parser = reqparse.RequestParser()
parser.add_argument('page', type=int, required=False)
parser.add_argument('per_page', type=int, required=False, choices=[5, 10, 20, 30, 40, 50])
parser.add_argument('publicId', type=str, required=False)

api = UsersDto.api

_insert_users = UsersDto.UsersPost
_fetch_users = UsersDto.UsersGet
_update_users = UsersDto.UsersPut
_delete_users = UsersDto.UsersDelete
_login_users = UsersDto.UserLogin


@api.route('/')
class Users(Resource):
    @api.expect(_insert_users, validate=True)
    @api.doc(security='apikey')
    @roles_required('ADMIN')
    def post(self):
        """Create a new User"""
        data = request.json
        return insert_users(data=data)

    @api.doc(security='apikey')
    @roles_required('ADMIN')
    @api.expect(_update_users, validate=True)
    def put(self):
        """Update User"""
        data = request.json
        return update_users(data=data)

    @api.doc(security='apikey')
    @roles_required('ADMIN')
    @api.expect(parser, validate=True)
    @api.marshal_list_with(_fetch_users, envelope='data')
    # @api.doc(security='apikey')
    # @roles_required('ADMIN', 'STUDENT')
    def get(self):
        """List all Users"""
        args = parser.parse_args()
        return fetch_users(data=args)

    @api.doc(security='apikey')
    @roles_required('ADMIN')
    @api.expect(_delete_users, validate=True)
    def delete(self):
        """Delete User"""
        data = request.json
        return delete_users(data=data)


@api.route('/login')
class Login(Resource):
    @api.expect(_login_users, validate=True)
    def post(self):
        """User login"""
        data = request.json
        return login_user(data=data)
