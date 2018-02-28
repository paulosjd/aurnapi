from flask_apispec import marshal_with
from flask_apispec.views import MethodResource
from app.models import Data
from app.schemas import DataSchema


@app.route('/pets')
@marshal_with(DataSchema(many=True))
def get_pets(**kwargs):
    return Pet.query.filter_by(**kwargs)