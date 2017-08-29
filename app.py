from flask import Flask
from models import db, Data, Sites
from bs4 import BeautifulSoup
from site_metadata import site_list
from get_data import hourly_data, format_data
import requests


app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)

def populate():
    with app.app_context():
        page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
        soup = BeautifulSoup(page, 'lxml')
        for site in site_list:
            site_data = Data(*format_data(hourly_data(soup, site)))
            db.session.add(site_data)
        db.session.commit()



"""
with app.app_context():
    site_list = Sites.query.all()
    ab = [a.name for a in site_list]
    print(ab)
"""
