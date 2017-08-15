from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources import Sites, Data
from site_lists import all_sites
from datetime import datetime
from no2_scraper import data_dict, info_dict

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


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

    def __init__(self, site, o3, no2, so2, pm25, pm10, time):
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
    time_string = site_column[6].text
    time = time_string[:10] + ' ' + time_string[10:]
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

    #site_info = info_dict.get(site)
    #site_data = data_dict.get(site)


    site_info = [site, url, lat, long]
    site_data = [o3_value, no2_value, so2_value, pm25_value, pm10_value]

    site_info_entry = Sites(*site_info)
    site_data_entry = Data(*site_data)

    db.session.add(site_info_entry)
    db.session.add(site_data_entry)

db.session.commit()

"""
mysites = ['Aberdeen']




site_info_list = [site, url, lat, long]
site_info_entry = Sites(*site_info_list)

site_data_values = [site, o3_value, no2_value, so2_value, pm25_value, pm10_value, time]



{'Aberdeen': {'name': 'Aberdeen',
              'url': 'http://www.defra....',
              'lat': '43.2353',
              'long': '8',
              'SO2': 'n/m',
              'Time': '06/08/201710:00:00'},


{'Aberdeen': {'NO2': '16',
              'O3': 'n/m',
              'PM10': '10',
              'PM2.5': '8',
              'SO2': 'n/m',
              'Time': '06/08/201710:00:00'},




db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="foo",
                     passwd="bar",
                     db="qoz")

cursor = db.cursor()


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    try:
        cursor.execute("SELECT * FROM items")
        ...

    except:
        print "Error: unable to fetch items"
    return jsonify({"desired: " response})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)

"""
