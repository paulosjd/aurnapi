from flask import Flask
from peewee import *
import sqlite3
from no2_scraper import no2_dict
#from pm_scraper import pm_dict
from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

app = Flask(__name__)


class No2Data(Base):
    __tablename__ = 'NO2Data'

    site = Column(String(100), primary_key=True)
    no2 = Column(Float(10), default='')
    time = Column(String(50), default='')


class PmData(Base):
    __tablename__ = 'PMData'

    site = Column(String(100), primary_key = True)
    pm10 = Column(Float(10), default='')
    pm25 = Column(Float(10), default='')
    time = Column(String(50), default='')


engine = create_engine('sqlite:///aurn-api.db')


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