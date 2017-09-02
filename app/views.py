from flask import jsonify, Blueprint
from .models import Sites, Data


first_blueprint = Blueprint('first', __name__)



@first_blueprint.route('/site-list')
@first_blueprint.route('/site-list/<site_type>')
def site_list(environ=None):
    site_environs = ['urban-traffic', 'urban-industrial', 'urban-background', 'suburban-background',
                  'suburban-industrial', 'background-rural']
    if environ in site_environs:
        site_table = Sites.query.filter_by(environ).all()
        return jsonify({a.name: a.id for a in site_table})
    elif environ == 'site-types':
        return jsonify({a.name: a.site_type for a in Sites.query.all()})
    else:
        return jsonify({a.name: a.id for a in Sites.query.all()})




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

