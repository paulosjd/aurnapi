from collections import Counter
from datetime import datetime, timedelta
from operator import itemgetter

from flask import Blueprint, jsonify
from sqlalchemy.sql.expression import cast
from sqlalchemy import desc, Integer

from app.models import HourlyData, db, Site
from app.schemas import current_hour_schema

misc_data = Blueprint('misc_data', __name__, url_prefix='/stats')


@misc_data.route('/highest/<pollutant>')
@misc_data.route('/highest/<pollutant>/<int:num>')
def highest(pollutant=None, num=None):
    field = getattr(HourlyData, pollutant) or HourlyData.pm10
    data = HourlyData.recent().order_by(field.cast(db.Integer).desc()).limit(num or 10)
    grouped = {}
    for a in data:
        date = a.time.split(' ')[0]
        date_val_pair = '-'.join(date.split('/')[::-1]), getattr(a, pollutant, 0)
        grouped.setdefault(a.owner.name, []).append(date_val_pair)
    json_data = {}
    for key in grouped:
        json_data[key] = {}
        counter = Counter([i[0] for i in grouped[key]])
        for date, val in grouped[key]:
            json_data[key][date] = {'counts': counter[date],
                                    'max': max([int(i[1]) for i in grouped[key] if i[1].isdigit()])}
    return jsonify(json_data)


@misc_data.route('/highest-sites/<pollutant>')
@misc_data.route('/highest-sites/<pollutant>/<int:num>')
def highest_sites(pollutant=None, num=None):
    field = getattr(HourlyData, pollutant) or HourlyData.pm10
    data = HourlyData.query.join(Site).filter(field != '')
    data = data.order_by(desc(cast(field, Integer))).limit(num or 500)
    grouped = {}
    for a in data:
        date = a.time.split(' ')[0]
        date_val_pair = '-'.join(date.split('/')[::-1]), getattr(a, pollutant, 0)
        grouped.setdefault(a.owner.name, []).append(date_val_pair)
    json_data = {}
    for key in grouped:
        json_data[key] = {}
        counter = Counter([i[0] for i in grouped[key]])
        for date, val in grouped[key]:
            json_data[key][date] = {'count': counter[date],
                                    'max': max([int(i[1]) for i in grouped[key] if i[1].isdigit() and i[0] == date])}
    return jsonify(
        sorted([{'name': k, 'date_counts': json_data[k]} for k, v in grouped.items()],
               key=itemgetter('name'))
    )

