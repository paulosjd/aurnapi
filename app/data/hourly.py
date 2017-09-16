from app.models import db, Data, Site
from .site_info import site_list, get_info, site_codes
from bs4 import BeautifulSoup
from datetime import datetime
import requests


"""def hourly_data(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return [o3, no2, so2, pm25, pm10, time]"""

def hourly_data2():
    #site_link = soup.find_all('a', string=site)[0]
    #row = site_link.findParent('td').findParent('tr').findAll('td')

    return {'ozone': '1', 'no2': '4', 'so2': '21', 'pm25': '12', 'pm10': '11', 'time': '16/09/2017 04:00:00'}


def validate_data(hourly_data_output):
    if hourly_data_output[5] != datetime.strftime((datetime.now().replace(microsecond=0, second=0, minute=0)),
                                                  "%d/%m/%Y %H:%M:%S"):
        return ['n/a'] * 5 + [datetime.strftime((datetime.now().replace(
                                                            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
    else:
        return hourly_data_output


def update_db():
    for site in Site.query.all():
        site_data = Data(owner=site, **hourly_data2())
        db.session.add(site_data)
    db.session.commit()


"""def populate():
    page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                        headers={'User-Agent': 'Not blank'}).content
    soup = BeautifulSoup(page, 'lxml')
    for site in site_list:
        site_instance = Site(*get_info(site))
        site_data = Data(*format_data(hourly_data(soup, site), owner=site_instance))
        #owner=site_instance and owner=site-instance  -  move to inside hourly_data() ?
        db.session.add(site_data)
    db.session.commit()"""

def create_db():
    #with app.app_context():
    db.create_all()
    for site in site_list:
        site_info = Site(*get_info(site))
        db.session.add(site_info)

    db.session.commit()

