from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    from .views.hourly_data import hourly_data
    from .views.sites_info import sites_info
    app.register_blueprint(hourly_data)
    app.register_blueprint(sites_info)
    db.init_app(app)
    with app.app_context():
        return app


def create_test_app():
    app = Flask(__name__)
    app.config.from_object('config.TestingConfig')
    db.init_app(app)
    app.app_context().push()
    return app
