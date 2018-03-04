from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False, unique=True)
    api_key = db.Column(db.String(64), unique=True, index=True)
    site_entry = db.relationship('Site', backref='user', lazy='dynamic')

    def __str__(self):
        return self.name


class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    site_code = db.Column(db.String(10), unique=True)
    region = db.Column(db.String(100))
    type = db.Column(db.String(100))
    defra_url = db.Column(db.String(250))
    map_url = db.Column(db.String(250))
    latitude = db.Column(db.String(50))
    longitude = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    hourly_data = db.relationship('HourlyData', backref='owner', lazy='dynamic')

    def __str__(self):
        return self.site_code


class DataMixin(object):
    ozone = db.Column(db.String(10), nullable=False)
    no2 = db.Column(db.String(10), nullable=False)
    so2 = db.Column(db.String(10), nullable=False)
    pm25 = db.Column(db.String(10), nullable=False)
    pm10 = db.Column(db.String(10), nullable=False)


class HourlyData(DataMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)

    @property
    def high_pm10(self):
        if self.pm10 > 25:
            return True


#class Exceedence(db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
  #  entry_id = db.Column(db.Integer, db.ForeignKey('hourlydata.id'), nullable=False)