from app.models import db, Data, Sites
from .site_info import site_list, get_info
from bs4 import BeautifulSoup
from datetime import datetime
import requests
from app import create_app

app = create_app()


def hourly_data(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return [site, o3, no2, so2, pm25, pm10, time]


def format_data(hourly_data_output):
    if hourly_data_output[6] != datetime.strftime((datetime.now().replace(microsecond=0, second=0, minute=0)),
                                                  "%d/%m/%Y %H:%M:%S"):
        return [hourly_data_output[0]] + ['n/a'] * 5 + [datetime.strftime((datetime.now().replace(
                                                            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
    else:
        return hourly_data_output


def populate():
    page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                        headers={'User-Agent': 'Not blank'}).content
    soup = BeautifulSoup(page, 'lxml')
    for site in site_list:
        site_data = Data(*format_data(hourly_data(soup, site)))
        db.session.add(site_data)
    db.session.commit()


def create_database():
    #with app.app_context():
    db.create_all()

    for site in site_list:  # only want to run once, not every time with data by CRON
        site_info = Sites(*get_info(site))
        db.session.add(site_info)

    db.session.commit()

