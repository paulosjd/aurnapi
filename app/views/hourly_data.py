from flask import jsonify, Blueprint
from app.models import Data, Site


hourly_data = Blueprint('hourly', __name__)

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


@hourly_data.route('/data/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper())
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/data/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*date)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/data/<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start = reversed(start.split('-'))
    end = reversed(end.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*start)
        end = '{}/{}/{} 00:00:00'.format(*end)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start, Data.time <= end)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/data/pollutants')
def pollutants():
    return jsonify({b: a for a, b in parameters.items()})
