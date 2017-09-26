
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # For working in PyCharm:
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
        # For working in PyCharm:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
