from collections import Counter

from flask import Blueprint, jsonify
from sqlalchemy.sql.expression import cast
from sqlalchemy import desc, Integer

from app.models import HourlyData, db, Site
from app.schemas import current_hour_schema

misc_data = Blueprint('misc_data', __name__, url_prefix='/stats')

@misc_data.route('/highest/<pollutant>/<int:num>')
def highest(pollutant=None, num=None):
    field = getattr(HourlyData, pollutant) or HourlyData.pm10
    data = HourlyData.query.filter(field != '')
    data = data.order_by(desc(cast(field, Integer))).limit(num or 10)
    return current_hour_schema.jsonify(data)

@misc_data.route('/highest-sites/<pollutant>')
@misc_data.route('/highest-sites/<pollutant>/<int:num>')
def highest_sites(pollutant=None, num=None):
    field = getattr(HourlyData, pollutant) or HourlyData.pm10
    data = HourlyData.query.join(Site).filter(field != '')
    data = data.order_by(desc(cast(field, Integer))).limit(num or 500)
    grouped = {}
    for a in data:
        date = a.time.split(' ')[0]
        grouped.setdefault(a.owner.name, []).append('-'.join(date.split('/')[::-1]))
    for key in grouped:
        grouped[key] = Counter(grouped[key])
    return jsonify(grouped)
