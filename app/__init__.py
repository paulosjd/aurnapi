from flask import Flask, jsonify
from .models import db, User
from flask_login import LoginManager, current_user, login_required


def create_app():
    app = Flask(__name__)
    app.config.from_object('config.DevelopmentConfig')
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    @login_manager.request_loader
    def load_user_from_request(request):
        api_key = request.headers.get('Authorization')
        if not api_key:
            return None
        return User.query.filter_by(api_key=api_key).first()
    from .data_views import hourly_data
    from .sites_info import sites_info
    app.register_blueprint(hourly_data)
    app.register_blueprint(sites_info)

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'message': str(error)}), 404

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({"error": "unauthorized"}), 401
    with app.app_context():
        return app


def create_test_app():
    app = Flask(__name__)
    app.config.from_object('config.TestingConfig')
    db.init_app(app)
    app.app_context().push()
    return app
