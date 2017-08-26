from flask import Flask
from flask_sqlalchemy import SQLAlchemy, _EngineConnector
from sqlalchemy import create_engine


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

    def __init__(self, o3, no2, so2, pm25, pm10, time):
        self.o3 = o3
        self.no2 = no2
        self.so2 = so2
        self.pm25 = pm25
        self.pm10 = pm10
        self.time = time


ab = Data.query.filter_by(pm25='4')
print((len(ab)))

if __name__ == '__main__':
    '__main__'


"""
from flask import Flask
from routes import get_pm10_blueprint


app = Flask(__name__)
app.register_blueprint(get_pm10_blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
    """