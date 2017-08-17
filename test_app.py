from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from site_metadata import site_list
from datetime import datetime
from test_models import Sites, Data, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True



db.init_app(app)


#can have all valuews e.g site, url, lat, long, o3_value etc importe from resources? Or even just a list of values which can unpack in the constuctor e.g. site values

mysites = ['Aberdeen', 'Oxford']
url_data = {'Aberdeen': 'defra-aber', 'Oxford': 'defra-ox'}
latitude = {'Aberdeen': '43.452', 'Oxford': '34.342'}
longitude = {'Aberdeen': '23.343', 'Oxford': '12.234'}
time_value = {'Aberdeen': '12:00', 'Oxford': '12:00'}
o3_value = {'Aberdeen': '12.3', 'Oxford': '12.8'}
no2_value = {'Aberdeen': '32', 'Oxford': '324'}
so2_value = {'Aberdeen': '23', 'Oxford': '31'}
pm25_value = {'Aberdeen': '53', 'Oxford': '124'}
pm10_value = {'Aberdeen': '43', 'Oxford': '17'}

for site in mysites:
    url = url_data.get(site)
    lat = latitude.get(site)
    long = longitude.get(site)
    time = time_value.get(site)
    o3 = o3_value.get(site)
    no2 = no2_value.get(site)
    so2 = so2_value.get(site)
    pm25 = pm25_value.get(site)
    pm10 = pm10_value.get(site)

    site_info = [site, url, lat, long]
    site_data = [site, o3, no2, so2, pm25, pm10, time]

    site_info_entry = Sites(*site_info)
    site_data_entry = Data(*site_data)


    db.session.add(site_info_entry)
    db.session.add(site_data_entry)


db.session.commit()
print(Data.query.get(1).pm25)

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