from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources import Sites, Data
from site_lists import all_sites
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(250))
    lat = Column(String(30))
    long = Column(String(30))

    def __init__(self, *args):
        self.name = name
        self.url = url
        self.lat = lat
        self.long = long


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100), db.ForeignKey('sites.name'))
    o3 = Column(String(10))
    no2 = Column(String(10))
    so2 = Column(String(10))
    pm10 = Column(String(10))
    pm25 = Column(String(10))
    time = Column(String(50))

    def __init__(self, *args):
        self.site = site
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time

        
db.create_all()

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')
#can have all valuews e.g site, url, lat, long, o3_value etc importe from resources? Or even just a list of values which can unpack in the constuctor e.g. site values
for site in all_sites:
    site_link = soup.find_all('a', string=site)[0]
    site_row = site_link.findParent('td').findParent('tr')
    site_column = site_row.findAll('td')
    url = ''
    lat = ''
    long = ''
    time = site_column[6].text.replace("2017","2017 " )
    o3_value = site_column[1].text.replace('\xa0', ' ').split(' ')[0]
    no2_value = site_column[2].text.replace('\xa0', ' ').split(' ')[0]
    so2_value = site_column[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25_value = site_column[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10_value = site_column[5].text.replace('\xa0', ' ').split(' ')[0]
    for value in site_values:
        if datetime.strptime(time, "%d/%m/%Y %H:%M:%S") != datetime.now().replace(microsecond=0, second=0, minute=0) \
                != datetime.now().replace(microsecond=0, second=0, minute=0):
            value = 'n/a'
        if value == 'n/m':
            value = 'n/a'
    site_info = [site, url, lat, long]
    site_data = [o3_value, no2_value, so2_value, pm25_value, pm10_value]

    site_info_entry = Sites(*site_info)
    site_data_entry = Data(*site_data)

    db.session.add(site_info_entry)
    db.session.add(site_data_entry)

db.session.commit()
