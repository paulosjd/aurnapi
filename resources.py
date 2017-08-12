from sqlalchemy import Column, Float, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class No2Data(Base):
    __tablename__ = 'NO2Data'

    site = Column(String(100), primary_key=True)
    no2 = Column(Float(10), default='')
    time = Column(String(50), default='')


class PmData(Base):
    __tablename__ = 'PMData'

    site = Column(String(100), primary_key = True)
    pm10 = Column(Float(10), default='')
    pm25 = Column(Float(10), default='')
    time = Column(String(50), default='')
