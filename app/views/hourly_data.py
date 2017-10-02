from flask import jsonify, Blueprint
from app.models import Data, Site

hourly_data = Blueprint('hourly', __name__)


@hourly_data.route('/data/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper())
    return jsonify({'data': [{'time': a.time, 'value': getattr(a, pollutant, a.PM10)} for a in queryset]})


@hourly_data.route('/data/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    try:
        start_time = '{}/{}/{} 00:00:00'.format(*date)
    except IndexError:
        return jsonify({'data': None})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start_time)
    return jsonify({'data': [{'time': a.time, 'value': getattr(a, pollutant, a.PM10)} for a in queryset]})


@hourly_data.route('/data/<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start_date = reversed(start.split('-'))
    end_date = reversed(end.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*start_date)
    end_time = '{}/{}/{} 00:00:00'.format(*end_date)
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start_time, Data.time <= end_time)
    return jsonify({'data': [{'time': a.time, 'value': getattr(a, pollutant, a.PM10)} for a in queryset]})


@hourly_data.route('/data/pollutants')
def pollutants():
    return jsonify({'ozone, µg/m3': 'ozone', 'nitrogen dioxide, µg/m3': 'NO2', 'sulfur dioxide, µg/m3': 'SO2',
                    'PM2.5 particles, µg/m3': 'PM25', 'PM10 particles, µg/m3': 'PM10'})
