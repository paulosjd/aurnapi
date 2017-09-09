from flask import jsonify, Blueprint
from .models import Sites, Data


sites_blueprint = Blueprint('sites', __name__)
data_blueprint = Blueprint('data', __name__)


@sites_blueprint.route('/site-list')
@sites_blueprint.route('/site-list/<environ>')
@sites_blueprint.route('/site-list/<region>')
def site_list(environ=None, region=None):
    site_environs = ['urban-traffic', 'urban-industrial', 'urban-background', 'suburban-background',
                     'suburban-industrial', 'rural-background']
    regions = ['greater-london', 'south-east', 'east-midlands', 'eastern', 'yorkshire', 'north-east', 'north-west',
               'west-midlands', 'south-west', 'south-wales', 'northern-ireland', 'north-east-scotland', 'north-wales',
               'highlands', 'scottish-borders', 'central-scotland']
    if environ in site_environs:
        return jsonify({a.name: a.site_code for a in Sites.query.filter_by(environ=environ).all()})
    if environ == 'site-environments':
        return jsonify({a.name: a.environ for a in Sites.query.all()})
    if region in regions:
        return jsonify({a.name: a.site_code for a in Sites.query.filter_by(region=region).all()})
    if region == 'site-regions':
        return jsonify({a.name: a.region for a in Sites.query.all()})
    else:
        return jsonify({a.name: a.site_code for a in Sites.query.all()})

#@sites_blueprint.route('<site_code>')
#def site_info(site_code=None):
 #   site_urls = Sites.query.all()
#    return jsonify(available attributes in Sites table)

@sites_blueprint.route('/site-geo')
def site_geo():
    return jsonify({a.name: a.lat + ", " + a.long for a in Sites.query.all()})

@sites_blueprint.route('/site-info')
def site_info():
    site_urls = Sites.query.all()
    return jsonify({a.name: a.url for a in site_urls})

###DO THE ABOVE FOR EACH OF SITE ATTRS


@data_blueprint.route('/<site_code>/<pollutant>')
def site_data(pollutant=None, site_code=None):
    pollutants = ['ozone', 'no2', 'so2', 'pm25', 'pm10']
    for n in pollutants:
        if pollutant == n:
            pollutant = n
    foo = Data.query.filter_by(site=site_code, pollutant=pollutant).all()

    return jsonify(foo[0].pm10)

#    foo = Data.query.filter_by(site=site_code).all()
#    return jsonify(foo[0].pm10)

@sites_blueprint.route('/pm10/<number>')
def site_pm10(number):
    foo = Data.query.filter_by(id=int(number)).all()
    return jsonify(foo[0].pm10)

