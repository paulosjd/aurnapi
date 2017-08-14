from sqlalchemy import Column, Float, String
from database import Base


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
