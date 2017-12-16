from flask import jsonify, Blueprint
from app.models import Data, Site
from app.views.current_data import make_site_dict


hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


@hourly_data.route('/<site_code>/<days>')
def site_aq_values(site_code, days):
    qs = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(days).all()
    if qs:
        data_keys = ['o3', 'no2', 'so2', 'pm10', 'pm25']
        data_list = [{'time': a.time, 'values': {b: getattr(a, b) for a in qs for b in data_keys}} for a in qs]
        all_data = {site_code.upper(): make_site_dict(site_code.upper(), data_list)}
        return jsonify(all_data)
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/<sc1>/<sc2>/<days>')
def two_sites_aq_values(sc1, sc2, days):
    qs1 = Data.query.join(Site).filter(Site.site_code == sc1.upper()).order_by(Data.id.desc()).limit(days).all()
    qs2 = Data.query.join(Site).filter(Site.site_code == sc2.upper()).order_by(Data.id.desc()).limit(days).all()
    if qs1 and qs2:
        data_keys = ['o3', 'no2', 'so2', 'pm10', 'pm25']
        data_list1 = [{'time': a.time, 'values': {b: getattr(a, b) for a in qs1 for b in data_keys}} for a in qs1]
        sc1_data = {sc1.upper(): make_site_dict(sc1.upper(), data_list1)}
        data_list2 = [{'time': a.time, 'values': {b: getattr(a, b) for a in qs2 for b in data_keys}} for a in qs2]
        sc2_data = {sc2.upper(): make_site_dict(sc2.upper(), data_list2)}
        return jsonify([sc1_data, sc2_data])
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/<name>/<pollutant>/<days>')
def hourly_data_2(name, pollutant, days):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper()).order_by(Data.id.desc()).limit(days*24)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})

@hourly_data.route('/pollutants')
def pollutants():
    return jsonify(parameters)