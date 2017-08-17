
#can have all valuews e.g site, url, lat, long, o3_value etc importe from resources? Or even just a list of values which can unpack in the constuctor e.g. site values


url_data = {'Aberdeen': 'defra-aber', 'Oxford': 'defra-ox'}
latitude = {'Aberdeen': '43.452', 'Oxford': '34.342'}
longitude = {'Aberdeen': '23.343', 'Oxford': '12.234'}
time_value = {'Aberdeen': '23.343', 'Oxford': '12.234'}
o3_value = {'Aberdeen': '12.3', 'Oxford': '12.8'}
no2_value = {'Aberdeen': '32', 'Oxford': '324'}
so2_value = {'Aberdeen': '23', 'Oxford': '31'}
pm25_value = {'Aberdeen': '53', 'Oxford': '124'}
pm10_value = {'Aberdeen': '43', 'Oxford': '17'}


def get_data_lists(site):
    url = url_data.get(site)
    lat = latitude.get(site)
    long = longitude.get(site)
    time = time_value.get(site)
    o3 = o3_value.get(site)
    no2 = no2_value.get(site)
    so2 = so2_value.get(site)
    pm25 = pm25_value.get(site)
    pm10 = pm10_value.get(site)
    site_info = [site, url, lat, long]
    site_data = [site, o3, no2, so2, pm25, pm10, time]
    return site_info, site_data
