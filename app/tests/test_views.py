import unittest
from app import create_test_app
from app.models import db, Data


class TestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_test_app()
        self.client = self.app.test_client()
        db.init_app(self.app)
        db.create_all()


    def test_db_entry(self):
        d = Data(site_code='ABD', ozone='10', NO2='20', SO2='30', PM25='40', PM10='50', time='10/09/2017 15:00:00')
        db.session.add(d)
        db.session.commit()
        self.assertGreater(d.id, 0)


    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == '__main__':
    unittest.main()
