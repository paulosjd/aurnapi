from flask import Flask, jsonify
from models import db, Sites, Data
from bs4 import BeautifulSoup
from site_metadata import site_list
from get_data import hourly_data, format_data
import requests


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

def populate():
    with app.app_context():
        page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
        soup = BeautifulSoup(page, 'lxml')
        for site in site_list:
            site_data = Data(*format_data(hourly_data(soup, site)))
            db.session.add(site_data)
        db.session.commit()

@app.route('/foo')
def not_found():
    return jsonify({'foo': 45})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
