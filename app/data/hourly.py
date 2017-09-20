from app.models import db, Data, Site
from .site_info import site_list, get_info
from bs4 import BeautifulSoup
from datetime import datetime
import requests


def hourly_data(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    ozone = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return {'ozone': ozone, 'no2': no2, 'so2': so2, 'pm25': pm25, 'pm10': pm10, 'time': time}


def validate_data(data_dict):
    hourly_dt = datetime.strftime(datetime.now().replace(microsecond=0, second=0, minute=0), "%d/%m/%Y %H:%M:%S")
    if data_dict['time'] != hourly_dt:
        na_values = ['n/a'] * 5 + [hourly_dt]
        return dict(zip(['ozone', 'no2', 'so2', 'pm25', 'pm10', 'time'], na_values))
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
