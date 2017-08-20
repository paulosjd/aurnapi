from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
from site_metadata import site_list, get_info
from get_data import hourly_data, format_data
import requests
from site_metadata import site_geo, site_urls
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)


class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    url = db.Column('url', db.String(250))
    lat = db.Column('latitude', db.String(30))
    long = db.Column('longitude', db.String(30))

    def __init__(self, name, url, lat, long):
        self.name = name
        self.url = url
        self.lat = lat
        self.long = long


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column('id', db.Integer, primary_key=True)
    site_name = db.Column('site', db.String(100), db.ForeignKey('sites.name'))
    o3 = db.Column('ozone', db.String(10))
    no2 = db.Column('no2', db.String(10))
    so2 = db.Column('so2', db.String(10))
    pm25 = db.Column('pm25', db.String(10))
    pm10 = db.Column('pm10', db.String(10))
    time = db.Column('time', db.String(50))

    def __init__(self, site_name, o3, no2, so2, pm25, pm10, time):
        self.site_name = site_name
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time


db.create_all()

for site in site_list:   # only want to run once, not every time with data by CRON
    site_info = Sites(*get_info(site))
    db.session.add(site_info)

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')


def hourly_data(row):
    o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return [o3, no2, so2, pm25, pm10, time]


def format_data(hourly_data_output):
    if hourly_data_output[5] != datetime.strftime((datetime.now().replace(microsecond=0, second=0, minute=0)),
                                                   "%d/%m/%Y %H:%M:%S"):
        return [''] * 5 + [datetime.strftime((datetime.now().replace(
                                                            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
    else:
        return hourly_data_output


def get_info(site):
    url = site_urls.get(site)
    lat = site_geo.get(site)[0]
    long = site_geo.get(site)[1]
    return [site, url, lat, long]

for site in site_list:
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    site_data = Data(*format_data(hourly_data(site, row)))
    db.session.add(site_data)

db.session.commit()


if __name__ == '__main__':
    '__main__'


