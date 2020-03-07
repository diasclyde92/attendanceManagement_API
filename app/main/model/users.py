from .. import mdb
import datetime

STATUS = ('ACTIVE', 'INACTIVE')
TYPES = ('EMPLOYEE', 'ADMIN')


class Name(mdb.EmbeddedDocument):
    firstName = mdb.StringField()
    lastName = mdb.StringField()


class Users(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    username = mdb.StringField()
    name = mdb.EmbeddedDocumentField(Name)
    email = mdb.EmailField()
    status = mdb.StringField(choices=STATUS, default='ACTIVE')
    userType = mdb.StringField(choices=TYPES, default='EMPLOYEE')
    password = mdb.StringField()
    passwordSalt = mdb.StringField()
    createdOn = mdb.DateTimeField(default=datetime.datetime.utcnow)
