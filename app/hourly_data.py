from flask import jsonify, Blueprint
from app.models import Data
import datetime


hourly_data = Blueprint('hourly', __name__)


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
