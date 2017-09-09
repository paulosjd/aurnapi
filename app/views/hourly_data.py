from flask import jsonify, Blueprint
from app.models import Data


hourly_data = Blueprint('hourly', __name__)


@hourly_data.route('/pm10/<name>/')
def all_data1(name):
    foo = Data.query.filter_by(site=name)
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/<start>/')
def all_data3(name, start):
    #e.g. start = 07-09-2017
    date = reversed(start.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*date)
    foo = Data.query.filter(Data.site == name, Data.time >= start_time)
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/<start>/<end>')
def all_data2(name, start, end):
    start_date = reversed(start.split('-'))
    end_date = reversed(end.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*start_date)
    end_time = '{}/{}/{} 00:00:00'.format(*end_date)
    foo = Data.query.filter(Data.site == name, Data.time >= start_time, Data.time <= end_time)
    return jsonify({a.time: a.pm10 for a in foo})

#once done all make way to do '/<pollutant>/.... instead repeating routes for each pollutant