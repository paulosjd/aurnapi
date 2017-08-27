from data_collector import db

class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(100))
    url = db.Column('url', db.String(250))
    lat = db.Column('latitude', db.String(30))
    long = db.Column('longitude', db.String(30))

    def __init__(self, name, url, lat, long):
        self.name = name
        self.url = url
        self.lat = lat
        self.long = long


class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column('id', db.Integer, primary_key=True)
    site = db.Column(db.String(100), db.ForeignKey('sites.name'))
    o3 = db.Column('ozone', db.String(10))
    no2 = db.Column('no2', db.String(10))
    so2 = db.Column('so2', db.String(10))
    pm25 = db.Column('pm25', db.String(10))
    pm10 = db.Column('pm10', db.String(10))
    time = db.Column('time', db.String(50))

    def __init__(self, site, o3, no2, so2, pm25, pm10, time):
        self.site = site
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time