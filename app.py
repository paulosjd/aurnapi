from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
from site_metadata import site_list, get_info
from scraper import get_data


#NEED TO DO PIP INSTALL REQUESTS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

#data_dict = dict(zip(all_sites, ['' for a in all_sites]))
#info_dict = dict(zip(all_sites, ['' for a in all_sites]))


class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    url = db.Column(db.String(250))
    lat = db.Column(db.String(30))
    long = db.Column(db.String(30))

    def __init__(self, name, url, lat, long):
        self.name = name
        self.url = url
        self.lat = lat
        self.long = long


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100), db.ForeignKey('sites.name'))
    o3 = db.Column(db.String(10))
    no2 = db.Column(db.String(10))
    so2 = db.Column(db.String(10))
    pm25 = db.Column(db.String(10))
    pm10 = db.Column(db.String(10))
    time = db.Column(db.String(50))

    def __init__(self, site: object, o3: object, no2: object, so2: object, pm25: object, pm10: object, time: object) -> object:
        self.site = site
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time

db.create_all()


for site in site_list:   # only want to run once, not every time with data by CRON
    get_info(site)
    site_info_entry = Sites(*site_info(site))
    db.session.add(site_info_entry)


page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')
for site in site_list:
    get_data(site, soup)
    site_data_entry = Data(*get_data(site))
    db.session.add(site_data_entry)

db.session.commit()

