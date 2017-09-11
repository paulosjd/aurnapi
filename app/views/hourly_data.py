from flask import jsonify, Blueprint
from app.models import Data


hourly_data = Blueprint('hourly', __name__)


@hourly_data.route('/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.filter_by(site_code=name)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})

@hourly_data.route('/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*date)
    queryset = Data.query.filter(Data.site_code == name, Data.time >= start_time)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})

@hourly_data.route('/<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start_date = reversed(start.split('-'))
    end_date = reversed(end.split('-'))
    start_time = '{}/{}/{} 00:00:00'.format(*start_date)
    end_time = '{}/{}/{} 00:00:00'.format(*end_date)
    queryset = Data.query.filter(Data.site_code == name, Data.time >= start_time, Data.time <= end_time)
    return jsonify({a.time: getattr(a, pollutant) for a in queryset})



"""

@hourly_data.route('/pm10/<name>/foo')
def all_data2(name):
    bar = datetime.datetime.now() - datetime.timedelta(days=5)
    foo = Data.query.filter(Data.site == name, Data.time <= bar)
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/foo')
def all_data2(name):
    bar = datetime.datetime.now() - datetime.timedelta(days=5)
    foo = Data.query.filter(Data.site == name, Data.time <= bar)
    return jsonify({a.time: a.pm10 for a in foo})


@hourly_data.route('/pm10/<name>/<day>')
def all_data1(name, day):
    foo = Data.query.filter(Data.site == name, Data.time == day + '/09/2017 16:00:00')




@hourly_data.route('/pm10/<name>/<int:days>')
def pm10_data_days(name, days):
    #period = datetime.datetime.now() - datetime.timedelta(days=days)

    #dt = datetime.datetime.strptime('07/09/2017 10:00:00', "%d/%m/%Y %H:%M:%S")
    foo = Data.query.filter_by(site=name).filter(dt < period).all()
    return jsonify({a.time: a.pm10 for a in foo})


@hourly_data.route('/days/<day>')
def all_data3(day):
    foo = Data.query.filter(Data.site == 'Thurrock', Data.time >= day + '/09/2017 17:00:00')
    return jsonify({a.time: a.pm10 for a in foo})


@hourly_data.route('/pm10/<name>/<date>')
def pm10_data_date(name, date):
    foo = Data.query.filter_by(site=name).filter(Data.time.split(' ')[0] == '06/09/2017').all()
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/<int:pm10value>')
def site_pm10(name, pm10value):
    foo = Data.query.filter_by(site=name, pm10=pm10value).all()
    return jsonify({a.time: a.pm10 for a in foo})
"""






"""@hourly_data.route('/pm10/<site_code>')
def site_pm10(site_code):
    foo = Data.query.filter_by(site_code=site_code).all()
    return jsonify(foo[0].pm10)"""
#once done all make way to do '/<pollutant>/.... instead repeating routes for each pollutant
