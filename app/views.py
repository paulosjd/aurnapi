from flask import jsonify, Blueprint
from .models import Sites, Data


first_blueprint = Blueprint('first', __name__)



@first_blueprint.route('/site-list')
@first_blueprint.route('/site-list/<site_type>')
def site_list(site_type=None):
    site_types = ['urban-traffic', 'urban-industrial', 'urban-background', 'suburban-background',
                  'suburban-industrial', 'background-rural']
    if site_type in site_types:
        site_table = Sites.query.filter_by(site_type).all()
        return jsonify({a.name: a.id for a in site_table})
    elif site_type == 'site-types':
        return jsonify({a.name: a.site_type for a in Sites.query.all()})
    else:
        return jsonify({a.name: a.id for a in Sites.query.all()})

##list of urban roadside sites, rural background etc.


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

