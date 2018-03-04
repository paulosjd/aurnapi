from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.models import db, Site, User
from app.schemas import site_schema, sites_schema, site_model_schema

site_views = Blueprint('Site', __name__, url_prefix='/sites')


@site_views.route("/")
def site_list():
    sites = Site.query.all()
    return sites_schema.jsonify(sites)


@site_views.route("/<int:id>")
def site_detail(id):
    site = Site.query.filter(Site.id == id).first_or_404()
    return site_schema.jsonify(site)


@site_views.route('/regions/<region>')
def site_views_filter(region):
    sites = Site.query.filter(Site.region == region).first_or_404()
    return sites_schema.jsonify(sites)


@site_views.route("/create", methods=["POST"])
@login_required
def create_site():
    api_key = request.headers.get('Authorization')
    user = User.query.filter_by(api_key=api_key).first()
    data, errors = site_schema.load(request.get_json())
    if errors:
        return jsonify(errors), 400

    db.session.add(Site(**data, user=user))
    db.session.commit()

    return jsonify({"message": "site created"}), 201


@site_views.route("/<int:id>", methods=["POST"])
@login_required
def edit_site(id):
    site = Site.query.filter(Site.id == id).first_or_404()
    site, errors = site_model_schema.load(request.get_json(), instance=site)
    if errors:
        return jsonify(errors), 400

    db.session.add(site)
    db.session.commit()

    return jsonify({"message": "site edited"}), 201


@site_views.route("/<int:id>", methods=["DELETE"])
@login_required
def remove_site(id):
    site = Site.query.filter(Site.id == id).first_or_404()
    db.session.delete(site)
    db.session.commit()
    return jsonify({"message": "deleted"})
