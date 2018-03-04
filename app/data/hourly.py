from app.models import db, HourlyData, Site
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import pytz
from app.data.sites import site_list


def get_hourly_data(soup, site):
    if soup.find_all('a', string=site):
        site_link = soup.find_all('a', string=site)[0]
        row = site_link.findParent('td').findParent('tr').findAll('td')
        aq_values = [row[n].text.replace('\xa0', ' ').split(' ')[0] for n in range(1,6)]
        hourly_data = dict(zip(['ozone', 'no2', 'so2', 'pm25', 'pm10'], aq_values))
        hourly_data['time'] = row[6].text[:10] + ' ' + row[6].text[10:]
        return hourly_data


def validate_data(data_dict):
    loc_dt = pytz.timezone('Europe/London').localize(datetime.now()) - timedelta(hours=1)
    hourly_dt = datetime.strftime(loc_dt.replace(microsecond=0, second=0, minute=0), "%d/%m/%Y %H:%M")
    if data_dict and data_dict['time'] != hourly_dt:
        na_values = ['n/a'] * 5 + [hourly_dt]
        return dict(zip(['ozone', 'no2', 'so2', 'pm25', 'pm10', 'time'], na_values))
    else:
        return data_dict


def update_db():
    page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                        headers={'User-Agent': 'Not blank'}).content
    soup = BeautifulSoup(page, 'lxml')
    for site in Site.query.filter(Site.name.in_(site_list)):
        data = validate_data(get_hourly_data(soup, site.name))
        if data:
            site_data = HourlyData(owner=site, **data)
            db.session.add(site_data)
            #if site_data.high_no2 is True:

    db.session.commit()
