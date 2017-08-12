from flask import Flask
from peewee import *
from no2_scraper import no2_dict
#from pm_scraper import pm_dict

app = Flask(__name__)

db = SqliteDatabase('aurn-api.db')


class No2Data(Model):
    site = CharField()
    no2 = FloatField()
    time = CharField()

    class Meta:
        database = db


class PmData(Model):
    site = CharField()
    pm10 = FloatField()
    pm25 = FloatField()
    time = CharField()

    class Meta:
        database = db


def initialize():
    """creates table and entry if they don't exist"""

    db.connect()
    db.create_tables([No2Data, PmData], safe=True)


def add_data():
    No2Data.create(**no2_dict)
    #PmData.create(pm_dict)


if __name__ == '__main__':
    initialize()
    add_data()

"""
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