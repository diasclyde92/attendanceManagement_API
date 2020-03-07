from .. import mdb
from .users import Users
import datetime


class AttendanceRecords(mdb.Document):
    publicId = mdb.UUIDField(binary=True)
    punchIn = mdb.DateTimeField()
    punchOut = mdb.DateTimeField()
    userId = mdb.ReferenceField(Users)
    adminUpdate = mdb.BooleanField(default=False)
    updatedBy = mdb.ReferenceField(Users)
    updatedOn = mdb.DateTimeField()

