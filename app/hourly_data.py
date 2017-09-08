from flask import jsonify, Blueprint
from app.models import Data, Sites
import datetime

hourly_data = Blueprint('hourly', __name__)



#@hourly_data.route('/ozone/<site-code>/<timeperiod>')
#def ozone_data(site-code):

    #    foo = Data.query.filter_by(site=site_code).all()
    #    return jsonify(foo[0].pm10)
    #return jsonify(foo[0].pm10)

#    foo = Data.query.filter_by(site=site_code).all()
#    return jsonify(foo[0].pm10)

@hourly_data.route('/pm10/<name>')
def all_data(name):
    foo = Data.query.filter_by(site=name).all()
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/<int:days>')
def pm10_data(name, days):
    period = datetime.timedelta(days=days)

    foo = Data.query.filter_by(site=name).all()
    return jsonify({a.time: a.pm10 for a in foo})

@hourly_data.route('/pm10/<name>/<int:pm10value>')
def site_pm10(name, pm10value):
    foo = Data.query.filter_by(site=name, pm10=pm10value).all()
    return jsonify({a.time: a.pm10 for a in foo})






"""@hourly_data.route('/pm10/<site_code>')
def site_pm10(site_code):
    foo = Data.query.filter_by(site_code=site_code).all()
    return jsonify(foo[0].pm10)"""
#once done all make way to do '/<pollutant>/.... instead repeating routes for each pollutant