import unittest

from app import create_app
from app.models import db, Data

app = create_app()

d = Data(site_code='ABD', ozone='10', no2='20', so2='30', pm25='40', pm10='50', time='10/09/2017 15:00:00')

def _init_database():
    db.session.add(d)
    db.session.commit(d)

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()
        db.create_all()
        _init_database()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
