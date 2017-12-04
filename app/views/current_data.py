from flask import jsonify, Blueprint
from app.models import Site, Current
from app.data.site_info import site_codes, get_info, site_list, site_names


current_data = Blueprint('current_data', __name__, url_prefix='/current-data')


def make_site_dict(site_code, aq_values):
    site_name = site_names.get(site_code)
    site_dict = {}
    site_info = get_info(site_name)
    del site_info['site_code']
    site_dict['info'] = site_info
    site_dict['latest_data'] = aq_values
    return site_dict


@current_data.route('/all-sites')
def all_recent_data():
    all_data = {}
    def get_current(site_code):
        current = Current.query.join(Site).filter(Site.site_code == site_code).first()
        return {'o3': current.o3, 'no2': current.no2, 'so2': current.so2, 'pm25': current.pm25, 'pm10': current.pm10}
    site_codes_list = [site_codes.get(b) for b in site_list]
    for a in site_codes_list:
        all_data[a] = make_site_dict(a, get_current(a))
    return jsonify(all_data)

