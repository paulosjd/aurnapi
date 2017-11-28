from flask import jsonify, Blueprint
from app.models import Data, Site, Current
from app.data.site_info import site_codes, get_info, site_list


hourly_data = Blueprint('hourly', __name__, url_prefix='/data')

parameters = {'o3': 'ozone, µg/m-3', 'no2': 'nitrogen dioxide, µg/m-3', 'so2': 'sulfur dioxide, µg/m-3',
              'pm25': 'PM2.5 particles, µg/m-3', 'pm10': 'PM10 particles, µg/m-3'}


@hourly_data.route('/recent/all-sites')
def all_recent_data():
    all_data = {}
    def get_current(site_code):
        current = Current.query.join(Site).filter(Site.site_code == site_code).first()
        return {'o3': current.o3, 'no2': current.no2, 'so2': current.so2, 'pm25': current.pm25, 'pm10': current.pm10}
    def make_dict(site_code):
        site_names = {i[1]: i[0] for i in site_codes.items()}
        site_name = site_names.get(site_code)
        site_dict = {}
        site_info = get_info(site_name)
        del site_info['site_code']
        site_dict['info'] = site_info
        site_dict['latest_data'] = get_current(site_code)
        return site_dict
    codes = [site_codes.get(b) for b in site_list]
    for a in codes:
        all_data[a] = make_dict(a)
    return jsonify(all_data)
    #catch exceptions e.g. no site name


@hourly_data.route('/<pollutant>/<name>/')
def hourly_data_1(pollutant, name):
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper())
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/<pollutant>/<name>/<start>/')
def hourly_data_2(pollutant, name, start):
    date = reversed(start.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*date)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('<pollutant>/<name>/<start>/<end>')
def hourly_data_3(pollutant, name, start, end):
    start = reversed(start.split('-'))
    end = reversed(end.split('-'))
    try:
        start = '{}/{}/{} 00:00:00'.format(*start)
        end = '{}/{}/{} 00:00:00'.format(*end)
    except IndexError:
        return jsonify({'message': 'no data'})
    queryset = Data.query.join(Site).filter(Site.site_code == name.upper(), Data.time >= start, Data.time <= end)
    if hasattr(queryset.first(), pollutant.lower()):
        return jsonify({'site': name.upper(), 'parameter': parameters.get(pollutant.lower()),
                        'data': [{'time': a.time, 'value': getattr(a, pollutant.lower(), None)} for a in queryset]})
    else:
        return jsonify({'message': 'no data'})


@hourly_data.route('/pollutants')
def pollutants():
    return jsonify({b: a for a, b in parameters.items()})
