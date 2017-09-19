from flask import jsonify, Blueprint
from app.models import Data, Site

hourly_data = Blueprint('hourly', __name__)


@hourly_data.route('/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})


@hourly_data.route('/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*date)
    queryset = Data.query.join(Site).filter(Site.site_code == name, Data.time >= start_time)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})


@hourly_data.route('/<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start_date = reversed(start.split('-'))
    end_date = reversed(end.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*start_date)
    end_time = '{}/{}/{} 00:00:00'.format(*end_date)
    queryset = Data.query.join(Site).filter(Site.site_code == name, Data.time >= start_time, Data.time <= end_time)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})