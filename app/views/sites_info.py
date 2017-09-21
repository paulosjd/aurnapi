from flask import jsonify, Blueprint
from app.models import Site, Data

sites_info = Blueprint('Site', __name__)


@sites_info.route('/site-list')
@sites_info.route('/site-list/<environ>')
@sites_info.route('/site-list/<region>')
def site_list(environ=None, region=None):
    site_environs = ['urban-traffic', 'urban-industrial', 'urban-background', 'suburban-background',
                     'suburban-industrial', 'rural-background']
    regions = ['greater-london', 'south-east', 'east-midlands', 'eastern', 'yorkshire', 'north-east', 'north-west',
               'west-midlands', 'south-west', 'south-wales', 'northern-ireland', 'north-east-scotland', 'north-wales',
               'highlands', 'scottish-borders', 'central-scotland']
    if environ in site_environs:
        return jsonify({a.name: a.site_code for a in Site.query.filter_by(environ=environ).all()})
    if environ == 'site-environments':
        return jsonify({a.name: a.environ for a in Site.query.all()})
    if region in regions:
        return jsonify({a.name: a.site_code for a in Site.query.filter_by(region=region).all()})
    if region == 'site-regions':
        return jsonify({a.name: a.region for a in Site.query.all()})
    else:
        return jsonify({a.name: a.site_code for a in Site.query.all()})


@sites_info.route('/site-geo')
def site_geo():
    return jsonify({a.name: a.lat + ", " + a.long for a in Site.query.all()})


@sites_info.route('/site-info')
def site_info():
    site_urls = Site.query.all()
    return jsonify({a.name: a.url for a in site_urls})


@sites_info.route('/site-maps')
def site_maps():
    map_urls = Site.query.all()
    return jsonify({a.name: a.map_url for a in map_urls})


@sites_info.route('/<site_code>')
def site_row(site_code):
    site = Site.query.filter_by(site_code=site_code).first()
    site_dict = {'site name': site.name, 'region': site.region, 'site environment': site.environ, 'site url': site.url,
                 'map url': site.map_url, 'latitude': site.lat, 'longitude': site.long}
    return jsonify(site_dict)


#change pm10 to <poll>
@sites_info.route('/available_data/<site_code>')
def available_data(site_code):
    qs = Site.query.join(Data).filter(Site.site_code == site_code).first()
    timepoints = []
    for a in qs.data:
        try:
            if int(a.pm10):
                timepoints.append(a.time)
        except ValueError:
            continue
    return jsonify([len(timepoints), timepoints[0], timepoints[-1]])
