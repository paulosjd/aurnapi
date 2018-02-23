from flask import jsonify, Blueprint
from app.models import Data, Site
from app.schemas import data_schema, site_schema

hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')


@hourly_data.route('/<site_code>/<days>')
def aq_data(site_code, days):
    data = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(days).all()
    return data_schema.jsonify(data)


@hourly_data.route('/site/<site_code>/<days>')
def nest_aq_data(site_code, days):
    data = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(days).all()
    return jsonify({'site info': site_schema.dump(data[0].owner), 'aq data': data_schema.dump(data)})



