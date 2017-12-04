from flask import jsonify, Blueprint
from app.models import Site
from app.data.site_info import get_info


sites_info = Blueprint('Site', __name__, url_prefix='/info')


@sites_info.route('/site-list/')
def site_list():
    return jsonify({a.name: a.site_code for a in Site.query.all()})


# to do: make possible to filter this list by below (e.g. site regions etc.) - then remove the below endpoints if redundant
@sites_info.route('/all-sites/')
def all_sites_info():
    d = {a.name: get_info(a.name) for a in Site.query.all()}
    for k, v in d.items():
        del v['name']
    return jsonify(d)


@sites_info.route('/site-regions')
@sites_info.route('/site-regions/<region>')
def site_regions(region=None):
    if region:
        return jsonify({a.name: a.site_code for a in Site.query.filter_by(region=region).all()})
    else:
        return jsonify(list(set([a.region for a in Site.query.all()])))


@sites_info.route('/site-environments')
@sites_info.route('/site-environments/<environ>')
def site_environs(environ=None):
    if environ:
        return jsonify({a.name: a.site_code for a in Site.query.filter_by(environ=environ).all()})
    else:
        return jsonify(list(set([a.environ for a in Site.query.all()])))


@sites_info.route('/site-info/<site_code>')
def site_row(site_code):
    site = Site.query.filter_by(site_code=site_code.upper()).first()
    try:
        site_dict = {'site name': site.name, 'region': site.region, 'site environment': site.environ,
                 'site url': site.url,
                 'map url': site.map_url, 'latitude': site.lat, 'longitude': site.long}
        return jsonify(site_dict)
    except AttributeError:
        return jsonify(None)


