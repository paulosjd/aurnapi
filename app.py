from flask import Flask
import sqlite3
from no2_scraper import no2_dict
#from pm_scraper import pm_dict
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/aurn-api.db'
db = SQLAlchemy(app)

class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(250))

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100), db.ForeignKey('sites.name'))
    no2 = Column(Float(10), default='')
    pm10 = Column(Float(10), default='')
    pm25 = Column(Float(10), default='')
    time = Column(String(50), default='')

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url


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