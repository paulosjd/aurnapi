from datetime import datetime
from site_metadata import site_geo, site_urls


def hourly_data(site, site_link):
    row = site_link.findParent('td').findParent('tr').findAll('td')
    o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    air = [o3, no2, so2, pm25, pm10, time]
    return ['n/a' for value in air[0:4] if datetime.strptime(air[5], "%d/%m/%Y %H:%M:%S") != datetime.now().replace(
        microsecond=0, second=0, minute=0) and value != 'n/m']

    #return [site, *air]


def get_info(site):
    url = site_urls.get(site)
    lat = site_geo.get(site)[0]
    long = site_geo.get(site)[1]
    return [site, url, lat, long]



"""for value in site_values:
    if datetime.strptime(time, "%d/%m/%Y %H:%M:%S") != datetime.now().replace(microsecond=0, second=0, minute=0):

    else:
        value.replace('n/m', 'n/a')"""