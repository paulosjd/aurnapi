

from peewee import *

db = MySQLDatabase
#db = SqliteDatabase('courses.sqlite')


class BaseClass(Model):
    class meta:
        database = db


class No2Data(BaseClass):
    site = CharField()
    no2 = FloatField()
    time = CharField()


class PmData(BaseClass):
    site = CharField()
    pm10 = FloatField()
    pm25 = FloatField()
    time = CharField()

def initialize():
    db.connect()
    db.create_tables([No2Data, PmData], safe=True)
    db.close()

