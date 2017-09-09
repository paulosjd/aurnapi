import unittest

from app import create_app

app = create_app()

class TestConfig(unittest.TestCase):
    def test_config_loading(self):
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite://'