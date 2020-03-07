from .. import mdb
import datetime


class Users(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    username = mdb.StringField()
    email = mdb.EmailField()