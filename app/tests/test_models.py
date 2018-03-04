import unittest
from app import create_test_app
from app.models import db, HourlyData, Site


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_test_app()
        self.client = self.app.test_client()
        db.init_app(self.app)
        db.create_all()


    def test_db_entry(self):
        s = Site(name='Aberdeen')
        d = HourlyData(owner=s, ozone='10', no2='20', so2='30', pm25='40', pm10='50', time='10/09/2017 15:00')
        db.session.add(d)
        db.session.commit()
        self.assertGreater(d.id, 0)


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
