from app.models import db, Data, Site
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import pytz


def hourly_data(soup, site):
    if soup.find_all('a', string=site):
        site_link = soup.find_all('a', string=site)[0]
        row = site_link.findParent('td').findParent('tr').findAll('td')
        o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
        no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
        so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
        pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
        pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
        time = row[6].text[:10] + ' ' + row[6].text[10:]
        return {'o3': o3, 'no2': no2, 'so2': so2, 'pm25': pm25, 'pm10': pm10, 'time': time}


def validate_data(data_dict):
    loc_dt = pytz.timezone('Europe/London').localize(datetime.now()) - timedelta(hours=1)
    hourly_dt = datetime.strftime(loc_dt.replace(microsecond=0, second=0, minute=0), "%d/%m/%Y %H:%M")
    if data_dict and data_dict['time'] != hourly_dt:
        na_values = ['n/a'] * 5 + [hourly_dt]
        return dict(zip(['o3', 'no2', 'so2', 'pm25', 'pm10', 'time'], na_values))
    else:
        return data_dict




