from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


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
    data = db.relationship('Data', backref='owner', lazy='dynamic')
    current = db.relationship('Current', backref='site', lazy='dynamic')

    def __str__(self):
        return self.site_code


class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    site_id = db.Column(db.Integer, db.ForeignKey('sites.id'), nullable=False)
    o3 = db.Column(db.String(10), nullable=False)
    no2 = db.Column(db.String(10), nullable=False)
    so2 = db.Column(db.String(10), nullable=False)
    pm25 = db.Column(db.String(10), nullable=False)
    pm10 = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(50), nullable=False)
