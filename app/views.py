from flask import jsonify, Blueprint
from .models import Sites, Data


first_blueprint = Blueprint('first', __name__)



@first_blueprint.route('/site-list')
@first_blueprint.route('/site-list/<environ>')
@first_blueprint.route('/site-list/<region>')
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


@first_blueprint.route('/site-geo')
def site_geo():
    return jsonify({a.name: a.lat + ", " + a.long for a in Sites.query.all()})

@first_blueprint.route('/site-info')
def site_info():
    site_urls = Sites.query.all()
    return jsonify({a.name: a.url for a in site_urls})

@first_blueprint.route('/<number>')
def site_data(number):
    foo = Sites.query.filter_by(id=int(number)).all()
    return jsonify(foo[0].name)

@first_blueprint.route('/pm10/<number>')
def site_pm10(number):
    foo = Data.query.filter_by(id=int(number)).all()
    return jsonify(foo[0].pm10)

