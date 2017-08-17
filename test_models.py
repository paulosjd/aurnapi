from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

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
