from flask import jsonify, Blueprint
from app.models import Data, Site
from app.views.current_data import make_site_dict


hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


#re-use make_site_dict but create a dict of pollutant {no2: {'11/10/2017 20 March 2017': '34', '':'' etc}, 'pm10: ''
@hourly_data.route('/<site_code>/<days>')
def hourly_data_new1(site_code, days):
    qs = Data.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(Data.id.desc()).limit(days).all()
    if qs:
        times = [a.time for a in qs]
        aq_data = {a: {} for a in times}
        all_data = {site_code.upper(): make_site_dict(site_code.upper(), aq_data)}

        return jsonify(all_data)
        #return jsonify({site_code.upper(): 'make_site_dict'})
        #return jsonify({site_code.upper(): {'site_info': {}, 'data': {}}})
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
    return jsonify({b: a for a, b in parameters.items()})
