from flask_restplus import Namespace, fields

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'X-API-KEY'
    }
}


class UsersDto:
    api = Namespace('users', authorizations=authorizations, description='User related operations')

    Name = api.model('Name', {
        'firstName': fields.String(),
        'lastName': fields.String()
    })

    UsersPost = api.model('UsersPost', {
        'username': fields.String(),
        'name': fields.Nested(Name),
        'userType': fields.String(),
        'email': fields.String(),
        # 'password': fields.String()
    })

    UsersPut = api.model('UsersPut', {
        'publicId': fields.String(),
        # 'username': fields.String(),
        'userType': fields.String(),
        'name': fields.Nested(Name),
        'email': fields.String(),
        'status': fields.String(),
    })

    UsersGet = api.model('UsersGet', {
        'publicId': fields.String(),
        'username': fields.String(),
        'name': fields.Nested(Name),
        'userType': fields.String(),
        'status': fields.String(),
        'email': fields.String()
    })

    UsersDelete = api.model('UsersDelete', {
        'publicId': fields.String()
    })

    UserLogin = api.model('UserLogin', {
        'username': fields.String(),
        'password': fields.String()
    })
