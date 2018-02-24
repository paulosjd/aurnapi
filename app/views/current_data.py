from flask import jsonify, Blueprint
from app.models import Site, Current
from app.schemas import data_schema

current_data = Blueprint('current_data', __name__, url_prefix='/current-data')


@current_data.route('/all-sites')
def all_current():
    current = Current.query.join(Site).filter(Site.site_code == site_code).first()
    return data_schema.jsonify(current)
