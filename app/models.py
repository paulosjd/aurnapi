from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    site_code = db.Column(db.String(10))
    region = db.Column(db.String(100))
    environ = db.Column('environment', db.String(100))
    url = db.Column(db.String(250))
    map_url = db.Column(db.String(250))
    lat = db.Column('latitude', db.String(50))
    long = db.Column('longitude', db.String(50))

    def __init__(self, name, site_code, region, environ, url, map_url, lat, long):
        self.name = name
        self.site_code = site_code
        self.region = region
        self.environ = environ
        self.url = url
        self.map_url = map_url
        self.lat = lat
        self.long = long


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    site_code = db.Column(db.String(100))
    ozone = db.Column(db.String(10))
    no2 = db.Column(db.String(10))
    so2 = db.Column(db.String(10))
    pm25 = db.Column(db.String(10))
    pm10 = db.Column(db.String(10))
    time = db.Column(db.String(50))

    def __init__(self, site_code, ozone, no2, so2, pm25, pm10, time):
        self.site_code = site_code
        self.ozone = ozone
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time
