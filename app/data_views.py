from flask import Blueprint, request, jsonify, url_for
from flask_login import login_required
from app.models import HourlyData, Site, db
from app.schemas import many_data_schema, data_schema, site_schema

hourly_data = Blueprint('hourly_data', __name__, url_prefix='/data')

"""
make yaml dict and copy in
:type: 'str' * 6
:param: 'integer of the measurement value', 'time in format %d/%m/%Y %H:%M'
"""

@hourly_data.route('/<site_code>/<num>')
def nest_aq_data(site_code, num):
    data = HourlyData.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(
        HourlyData.id.desc()).limit(num).all()
    return jsonify({'site info': site_schema.dump(data[0].owner), 'aq data': many_data_schema.dump(data)})


@hourly_data.route("/<site_code>", methods=["POST"])
@login_required
def create_hourly(site_code):
    site = Site.query.filter(Site.site_code == site_code).first()
    data, errors = data_schema.load(request.get_json())
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(HourlyData(**data, owner=site))
    db.session.commit()

    resp = jsonify({"message": "created"})
    resp.status_code = 201
    return resp


@hourly_data.route("/<int:id>", methods=["POST"])
@login_required
def edit_site(id):
    site = Site.query.filter(Site.id==id).first_or_404()
    # instance tells Marshmallow to edit existing entry instead of creating new one
    site, errors = site_schema.load(request.get_json(), instance=site)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(site)
    db.session.commit()

    resp = jsonify({"message": "updated"})
    resp.status_code = 201
    location = url_for("Site.site_detail", id=site.id)
    resp.headers["Location"] = location
    return resp


@hourly_data.route("/<int:id>", methods=["DELETE"])
@login_required
def remove_site(id):
    site = Site.query.filter(Site.id == id).first_or_404()
    db.session.delete(site)
    db.session.commit()
    return jsonify({"message": "deleted"})


"""
@hourly_data.route('/<site_code>/<num>')
def aq_data(site_code, num):
    data = HourlyData.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(
        HourlyData.id.desc()).limit(num).all()
    return many_data_schema.jsonify(data)


@hourly_data.route('/bar/<site_code>/<num>')
def hourly_aq(site_code, num):
    qs = HourlyData.query.join(Site).filter(Site.site_code == site_code.upper()).order_by(
        HourlyData.id.desc()).limit(num).all()
    if qs:
        fields = ['o3', 'no2', 'so2', 'pm10', 'pm25']
        aq_data = [{'time': obj.time, 'values': {a: getattr(obj, a) for obj in qs for a in fields}} for obj in qs]
        site_fields = ['name', 'site_code', 'region', 'lat', 'long']
        all_data = {'site_info': {a: getattr(qs[0].owner, a) for a in site_fields}, 'aq_data': aq_data}
        return jsonify(all_data)
    return jsonify({'message': 'no data'})
"""