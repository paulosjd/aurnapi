from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    api_key = db.Column(db.String(64), unique=True, index=True)


class Site(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    site_code = db.Column(db.String(10), unique=True)
    region = db.Column(db.String(100))
    environ = db.Column('environment', db.String(100))
    url = db.Column(db.String(250))
    map_url = db.Column(db.String(250))
    lat = db.Column('latitude', db.String(50))
    long = db.Column('longitude', db.String(50))
    hourly = db.relationship('HourlyData', backref='owner', lazy='dynamic')

    @property
    def url(self):
        return url_for("get_site", id=self.id)

    def __str__(self):
        return self.site_code


class DataMixin(object):
    o3 = db.Column(db.String(10), nullable=False)
    no2 = db.Column(db.String(10), nullable=False)
    so2 = db.Column(db.String(10), nullable=False)
    pm25 = db.Column(db.String(10), nullable=False)
    pm10 = db.Column(db.String(10), nullable=False)


class HourlyData(DataMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(20), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
