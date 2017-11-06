
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
    # For working in PyCharm:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    TESTING = False
    MAIL_SERVER = '.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_DEBUG = True
    MAIL_USERNAME = 'gmail.com'
    MAIL_PASSWORD = ''
    MAIL_DEFAULT_SENDER = 'mail.com'
    MAIL_MAX_EMAILS = None
    MAIL_SUPPRESS_SEND = False
    MAIL_ASCII_ATTACHMENTS = False


class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db'
        # For working in PyCharm:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
