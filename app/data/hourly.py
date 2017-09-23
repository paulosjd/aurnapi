from app.models import db, Data, Site
from .site_info import site_list, get_info
from bs4 import BeautifulSoup
from datetime import datetime
import requests


def hourly_data(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    ozone = row[1].text.replace('\xa0', ' ').split(' ')[0]
    NO2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    SO2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    PM25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    PM10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return {'ozone': ozone, 'NO2': NO2, 'SO2': SO2, 'PM25': PM25, 'PM10': PM10, 'time': time}

##will work if just have     PM10 = row[5].text.split('\xa0')[0] instead??

def hourly_data2(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    values = [x.text.replace('\xa0', ' ').split(' ')[0] for x in row[1:5]] + time
    keys = ['ozone', 'NO2', 'SO2', 'PM25', 'PM10', 'time']
    return dict(zip(keys, values))

def hourly_data3(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    ozone = row[1].text.split('\xa0')[0]
    NO2 = row[2].text.split('\xa0')[0]
    SO2 = row[3].text.split('\xa0')[0]
    PM25 = row[4].text.split('\xa0')[0]
    PM10 = row[5].text.split('\xa0')[0]
    time = row[6].text.split('\xa0')[0]
    return {'ozone': ozone, 'NO2': NO2, 'SO2': SO2, 'PM25': PM25, 'PM10': PM10, 'time': time}


def hourly_data4(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    ozone = row[1].text.split('\xa0')[0]
    NO2 = row[2].text.split('\xa0')[0]
    SO2 = row[3].text.split('\xa0')[0]
    PM25 = row[4].text.split('\xa0')[0]
    PM10 = row[5].text.split('\xa0')[0]
    time = row[6].text.split('\xa0')[0]
    return {'ozone': ozone, 'NO2': NO2, 'SO2': SO2, 'PM25': PM25, 'PM10': PM10, 'time': time}


def validate_data(data_dict):
    hourly_dt = datetime.strftime(datetime.now().replace(microsecond=0, second=0, minute=0), "%d/%m/%Y %H:%M:%S")
    if data_dict['time'] != hourly_dt:
        na_values = ['n/a'] * 5 + [hourly_dt]
        return dict(zip(['ozone', 'NO2', 'SO2', 'PM25', 'PM10', 'time'], na_values))
    else:
        return data_dict


def update_db():
    page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                        headers={'User-Agent': 'Not blank'}).content
    soup = BeautifulSoup(page, 'lxml')
    for site in Site.query.all():
        data = validate_data(hourly_data(soup, site.name))
        site_data = Data(owner=site, **data)
        db.session.add(site_data)
    db.session.commit()


def create_db():
    db.create_all()
    for site in site_list:
        site_info = Site(**get_info(site))
        db.session.add(site_info)
    db.session.commit()
