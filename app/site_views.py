from flask import Blueprint, request, jsonify, url_for
from app.models import Site, db
from app.schemas import site_schema, sites_schema
from flask_login import login_required

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
    site, errors = site_schema.load(request.form)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(site)
    db.session.commit()

    resp = jsonify({"message": "created"})
    resp.status_code = 201
    location = url_for("site_detail", id=site.id)
    resp.headers["Location"] = location
    return resp


@site_views.route("/<int:id>", methods=["POST"])
@login_required
def edit_site(id):
    site = Site.query.filter(Site.id==id).first_or_404()
    site, errors = site_schema.load(request.form, instance=site)
    if errors:
        resp = jsonify(errors)
        resp.status_code = 400
        return resp

    db.session.add(site)
    db.session.commit()

    resp = jsonify({"message": "updated"})
    resp.status_code = 201
    location = url_for("site_detail", id=site.id)
    resp.headers["Location"] = location
    return resp


@site_views.route("/<int:id>", methods=["DELETE"])
@login_required
def remove_site(id):
    site = Site.query.filter(Site.id == id).first_or_404()
    db.session.delete(site)
    db.session.commit()
    return jsonify({"message": "deleted"})
