from flask import Flask
from .models import db


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    from .views.hourly_data import hourly_data
    from .views.sites_info import sites_info
    app.register_blueprint(hourly_data)
    app.register_blueprint(sites_info)
    db.init_app(app)
    with app.app_context():
        return app

