
class DevelopmentConfig:
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # For working in PyCharm:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig:
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
