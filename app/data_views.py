from flask import Blueprint, request, jsonify
from flask_login import login_required
from flasgger.utils import swag_from
from app.models import HourlyData, Site, db
from app.schemas import current_hour_schema, many_data_schema, data_schema, hourlydata_schema, site_schema

hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')


@hourly_data.route('/')
@swag_from('specs/recent_aq.yml')
def recent_aq():
    data = HourlyData.query.group_by(HourlyData.site_id)
    return current_hour_schema.jsonify(data)


@hourly_data.route('/<site_code>/<number>')
@swag_from('specs/get_aq_data.yml')
def get_aq_data(site_code, number):
    data = HourlyData.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(
        HourlyData.id.desc()).limit(number).all()
    return jsonify({'site info': site_schema.dump(data[0].owner), 'aq data': many_data_schema.dump(data)})


@hourly_data.route("/<site_code>", methods=["POST"])
@login_required
@swag_from('specs/create_hourly.yml')
def create_hourly(site_code):
    site = Site.query.filter(Site.site_code == site_code).first()
    data, errors = data_schema.load(request.get_json())
    if errors:
        return jsonify(errors), 400
    db.session.add(HourlyData(**data, owner=site))
    db.session.commit()
    resp = jsonify({"message": "created"})
    resp.status_code = 201
    return resp


@hourly_data.route("/<int:id>", methods=["POST"])
@login_required
@swag_from('specs/edit_hourly.yml')
def edit_hourly(id):
    entry = HourlyData.query.filter(HourlyData.id==id).first_or_404()
    data, errors = hourlydata_schema.load(request.get_json(), instance=entry)
    if errors:
        return jsonify(errors), 400
    db.session.add(data)
    db.session.commit()
    return jsonify({"message": "updated"}), 201


@hourly_data.route("/<int:id>", methods=["DELETE"])
@login_required
def remove_hourly(id):
    data = HourlyData.query.filter(HourlyData.id == id).first_or_404()
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": "deleted"})


"""
@hourly_data.route('/<site_code>/<num>')
def aq_data(site_code, num):
    data = HourlyData.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(
        HourlyData.id.desc()).limit(num).all()
    return many_data_schema.jsonify(data)

"""