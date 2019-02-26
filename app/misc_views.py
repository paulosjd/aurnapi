from flask import Blueprint
from app.models import HourlyData, db
from app.schemas import current_hour_schema

misc_data = Blueprint('misc_data', __name__, url_prefix='/stats')


@misc_data.route('/highest/<pollutant>/<int:num>')
def highest(pollutant=None, num=None):
    field = getattr(HourlyData, pollutant) or HourlyData.pm10
    data = HourlyData.query.order_by(field.cast(db.Integer).desc()).limit(num or 10)
    return current_hour_schema.jsonify(data)
