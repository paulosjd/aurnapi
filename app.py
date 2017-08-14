from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from resources import Sites, Data


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

    def __init__(self, name=None, url=None, lat=None, long=None):
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

    def __init__(self, site=None, o3=None, no2=None, so2=None, pm10=None, pm25=None, time=None):
        self.site = site
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time
      

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
