from flask import jsonify, Blueprint
from app.models import Site, Data

sites_info = Blueprint('Site', __name__)

@sites_info.route('/site-list/')
def site_list():
    return jsonify({a.name: a.site_code for a in Site.query.all()})


@sites_info.route('/available-data/<pollutant>/<site_code>')
def available_data(pollutant, site_code):
    qs = Site.query.join(Data).filter(Site.site_code == site_code.upper()).first()
    if hasattr (qs, pollutant.upper()):
        times = []
        for a in qs.data:
            #to discount 'n/a' and 'n/m' values
            try:
                if int(getattr(a, pollutant.upper())):
                    times.append(a.time)
            except AttributeError:
                continue
            except ValueError:
                continue
        return jsonify([str(len(times)), times[0], times[-1]])
    else:
        return jsonify(None)


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


@sites_info.route('/site-geo')
def site_geo():
    return jsonify({a.name: a.lat + ", " + a.long for a in Site.query.all()})


@sites_info.route('/site-url')
def site_url():
    site_urls = Site.query.all()
    return jsonify({a.name: a.url for a in site_urls})


@sites_info.route('/site-maps')
def site_maps():
    map_urls = Site.query.all()
    return jsonify({a.name: a.map_url for a in map_urls})


