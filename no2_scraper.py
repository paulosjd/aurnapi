import requests
from bs4 import BeautifulSoup
from datetime import datetime
from site_lists import all_sites


data_dict = dict(zip(all_sites, ['' for a in all_sites]
info_dict = dict(zip(all_sites, ['' for a in all_sites]

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')
#can have all valuews e.g site, url, lat, long, o3_value etc importe from resources? Or even just a list of values which can unpack in the constuctor e.g. site values
for site in all_sites:
    site_link = soup.find_all('a', string=site)[0]
    site_row = site_link.findParent('td').findParent('tr')
    site_column = site_row.findAll('td')
    url = ''
    lat = ''
    long = ''
    time_string = site_column[6].text
    time = time_string[:10] + ' ' + time_string[10:]
    o3_value = site_column[1].text.replace('\xa0', ' ').split(' ')[0]
    no2_value = site_column[2].text.replace('\xa0', ' ').split(' ')[0]
    so2_value = site_column[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25_value = site_column[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10_value = site_column[5].text.replace('\xa0', ' ').split(' ')[0]
    for value in site_values:
        if datetime.strptime(time, "%d/%m/%Y %H:%M:%S") != datetime.now().replace(microsecond=0, second=0, minute=0) \
                != datetime.now().replace(microsecond=0, second=0, minute=0):
            value = 'n/a'
        if value == 'n/m':
            value = 'n/a'
    site_info = [site, url, lat, long]
    site_data = [o3_value, no2_value, so2_value, pm25_value, pm10_value]
    info_dict.update(site, site_info)
    data_dict.update(site, site_data)

