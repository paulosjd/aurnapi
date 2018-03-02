from flask import jsonify, Blueprint
from flask_login import current_user
from app.models import Data, Site
from app.schemas import data_schema, site_schema

hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')


@hourly_data.route("/whoami")
def who_am_i():
    """  Test it out:
    $ curl localhost:5000/whoami
    { "name": "anonymous")
      After creating User:
    $ curl localhost:5000/whoami -H "Authorization: abc123"
    { "name": "Gary Larry") """
    if current_user.is_authenticated:
        name = current_user.name
    else:
        name = "anonymous"
    return jsonify({"name": name})


@hourly_data.route('/<site_code>/<num>')
def aq_data(site_code, num):
    data = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(num).all()
    return data_schema.jsonify(data)




@hourly_data.route('/site/<site_code>/<num>')
def nest_aq_data(site_code, num):
    data = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(num).all()
    return jsonify({'site info': site_schema.dump(data[0].owner), 'aq data': data_schema.dump(data)})


@hourly_data.route('/bar/<site_code>/<num>')
def hourly_aq(site_code, num):
    qs = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(num).all()
    if qs:
        fields = ['o3', 'no2', 'so2', 'pm10', 'pm25']
        aq_data = [{'time': obj.time, 'values': {a: getattr(obj, a) for obj in qs for a in fields}} for obj in qs]
        site_fields = ['name', 'site_code', 'region', 'lat', 'long']
        all_data = {'site_info': {a: getattr(qs[0].owner, a) for a in site_fields}, 'aq_data': aq_data}
        return jsonify(all_data)
    return jsonify({'message': 'no data'})


"""
@hourly_data.route('/all-sites')
def all_current():
    current = Current.query.join(Site).filter(Site.site_code == site_code).first()
    return data_schema.jsonify(current)
"""


