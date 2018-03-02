import sys
from flask import jsonify
from flask_login import LoginManager
from app.models import User
from app import create_app
from app.data.sites import create_db
from app.data.hourly import update_db
from app.data_views import hourly_data
from app.site_views import site_views

application = create_app()
application.register_blueprint(hourly_data)
application.register_blueprint(site_views)

login_manager = LoginManager()
login_manager.init_app(application)


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if not api_key:
        return None
    return User.query.filter_by(api_key=api_key).first()


@application.errorhandler(404)
def not_found(error):
    return jsonify({'message': str(error)}), 404


@application.errorhandler(401)
def unauthorized(error):
    return jsonify({"error": "unauthorized"}), 401


if __name__ == '__main__':
    if "createdb" in sys.argv:
        with application.app_context():
            create_db()
    elif "collectdata" in sys.argv:
        with application.app_context():
            update_db()
    else:
        application.run(debug=True)
