from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from bs4 import BeautifulSoup
from data_collector.site_metadata import site_list, get_info
from data_collector.get_data import hourly_data, format_data
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


from data_collector.models import Sites, Data



for site in site_list:   # only want to run once, not every time with data by CRON
    site_info = Sites(*get_info(site))
    db.session.add(site_info)

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')

for site in site_list:
    site_data = Data(*format_data(hourly_data(soup, site)))
    db.session.add(site_data)

db.session.commit()

#first = Data.query.first()
#print(dir(first))
#print(first.o3)
#print(first.time)

#mids = Data.query.get(8)
#print(dir(mids))
#print(mids.pm10)

#pet = Data.query.filter_by(pm25='4').all()
#print(len(pet))
#3

#pet = Data.query.filter_by(pm25='4').all()
#print(dir(pet[1]))

#pet = Data.query.filter_by(pm25='4').all()
#print(pet[1].pm10)

@app.route('/not-found')
def not_found():
    return jsonify()

#if __name__ == "__main__":
 #   "__main__"
    # app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)



