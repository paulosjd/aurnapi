import sys
from flask import Flask, jsonify
from flask_login import LoginManager
from apispec import APISpec
from app.models import db, User
from app.schemas import DataSchema
from flask_apispec.extension import FlaskApiSpec
from app import create_app
from app.data.sites import create_db
from app.data.hourly import update_db

application = create_app()

from apispec import APISpec

spec = APISpec(
    title='Gisty',
    version='1.0.0',
    info=dict(
        description='A minimal gist API'
    ),
    plugins=[
        'apispec.ext.flask',
        'apispec.ext.marshmallow'
    ]
)
spec.definition('Gist', schema=DataSchema)
print(spec.to_dict())
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


from app.data_views import hourly_data
from app.sites_info import sites_info

application.register_blueprint(hourly_data)
application.register_blueprint(sites_info)


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