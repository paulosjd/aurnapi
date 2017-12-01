from flask import jsonify, Blueprint
from app.models import Data, Site
from datetime import datetime

hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


@hourly_data.route('/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper())
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/<pollutant>/<name>/<days>')
def hourly_data_2(pollutant, name, days):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper()).order_by(Data.id.desc()).limit(days)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/pollutants')
def pollutants():
    return jsonify({b: a for a, b in parameters.items()})
