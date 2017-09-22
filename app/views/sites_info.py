from flask import jsonify, Blueprint
from app.models import Site, Data

sites_info = Blueprint('Site', __name__)


# site-list/urban-traffic RETURNS ALL 123 SITES
# BUT site-list/urban-traffic/<REGION> DOES NOT

# concisify the following using getattr()??  --for a.environ and a.region
# remove the 2 lists??
#   - instead of e.g. if region in regions:, just have if hasattr(): ?

@sites_info.route('/site-list/')
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
    if region in regions:
        return jsonify({a.name: a.site_code for a in Site.query.filter_by(region=region).all()})
    else:
        return jsonify({a.name: a.site_code for a in Site.query.all()})


@sites_info.route('/<site_code>')
def site_row(site_code):
    site = Site.query.filter_by(site_code=site_code).first()
    site_dict = {'site name': site.name, 'region': site.region, 'site environment': site.environ,
                 'site url': site.url,
                 'map url': site.map_url, 'latitude': site.lat, 'longitude': site.long}
    return jsonify(site_dict)


# getattr(a, pollutant) is equivalent to a.pollutant (where 'a' has no attribute pollutant)
@sites_info.route('/available-data/<pollutant>/<site_code>')
def available_data(pollutant, site_code):
    qs = Site.query.join(Data).filter(Site.site_code == site_code).first()
    times = []
    for a in qs.data:
        try:
            if int(getattr(a, pollutant)):
                times.append(a.time)
        except ValueError:
            continue
    try:
        return jsonify([str(len(times)), times[0], times[-1]])
    except IndexError:
        return jsonify('no data')


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
