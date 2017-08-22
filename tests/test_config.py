import unittest

from . import app

class TestConfig(unittest.TestCase):
    def test_config_loading(self):
        assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite://'
        
if __name__ = "__main__":
    unittest.main()
    
