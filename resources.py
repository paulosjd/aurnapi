from sqlalchemy import Column, Float, String
from database import Base


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
    o3 = Column(Float(10))
    no2 = Column(Float(10))
    so2 = Column(Float(10))
    pm10 = Column(Float(10))
    pm25 = Column(Float(10))
    time = Column(String(50))

    def __init__(self, site=None, no2=None, pm10=None, pm25=None, time=None):
        self.site = site
        self.no2 = no2
        self.pm10 = pm10
        self.pm25 = pm25
        self.time = time
