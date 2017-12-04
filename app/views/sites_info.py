from flask import jsonify, Blueprint
from app.models import Site
from app.data.site_info import get_info


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


@sites_info.route('/<region>')
def info_by_region():
    info = {a.name: get_info(a.name) for a in Site.query.all()}
    if info:
        for k, v in info.items():
            del v['name']
        return jsonify(info)
    else:
        return jsonify({'message': 'no data'})


@sites_info.route('/<environ>')
def info_by_environment_type():
    info = {a.name: get_info(a.name) for a in Site.query.all()}
    if info:
        for k, v in info.items():
            del v['name']
        return jsonify(info)
    else:
        return jsonify({'message': 'no data'})
