from flask import Flask, jsonify
from flask_login import LoginManager
from apispec import APISpec
from .models import db, User
from .schemas import DataSchema
from flask_apispec.extension import FlaskApiSpec



def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')

    db.init_app(app)

    with app.app_context():
        return app


def create_test_app():
    app = Flask(__name__)
    app.config.from_object('config.TestingConfig')
    db.init_app(app)
    app.app_context().push()
    return app
