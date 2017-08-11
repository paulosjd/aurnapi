from flask import Flask
from peewee import *

app = Flask(__name__)

db = SqliteDatabase('aurn-api.db')


class BaseClass(Model):

    class Meta:
        database = db


def initialize():
    """creates table and entry if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


class No2Data(BaseClass):
    site = CharField()
    no2 = FloatField()
    
    time = CharField()


class PmData(BaseClass):
    site = CharField()
    pm10 = FloatField()
    pm25 = FloatField()
    time = CharField()


if __name__ == '__main__':
    initialize()
