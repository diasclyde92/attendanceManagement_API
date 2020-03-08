import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', '0Ngu@Rd_N3Xt+GeN3RaT10n')
    DEBUG = False


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'attendance_management'}
    SECRET_KEY = 'flask+mongoengine=<3'


class TestingConfig(Config):
    DEBUG = False
    TESTING = True
    MONGODB_SETTINGS = {'DB': 'attendance_management_test'}
    SECRET_KEY = 'flask+mongoengine=<3'


config_by_name = dict(
    DEV=DevelopmentConfig,
    TEST=TestingConfig
)

key = Config.SECRET_KEY
