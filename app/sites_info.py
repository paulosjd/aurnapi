from flask import jsonify, Blueprint
from app.models import Site
from app.data.sites import get_info

sites_info = Blueprint('Site', __name__, url_prefix='/info')


@sites_info.route('/site-list/')
def site_list():
    return jsonify({a.name: a.site_code for a in Site.query.all()})


@sites_info.route('/all-sites')
def all_sites_info():
    info = {a.name: get_info(a.name) for a in Site.query.all()}
    for k, v in info.items():
        del v['name']
    return jsonify(info)


@sites_info.route('/<region_or_environ>')
def sites_info_filter(region_or_environ):
    region_info = {a.name: get_info(a.name) for a in Site.query.filter_by(region=region_or_environ)}
    environ_info = {a.name: get_info(a.name) for a in Site.query.filter_by(environ=region_or_environ)}
    if region_info:
        for k, v in region_info.items():
            del v['name']
        return jsonify(region_info)
    elif environ_info:
        for k, v in environ_info.items():
            del v['name']
        return jsonify(environ_info)
    else:
        return jsonify({'message': 'no data'})
