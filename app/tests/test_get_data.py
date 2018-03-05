from app.data.collect_data import get_hourly_data, validate_data

from bs4 import BeautifulSoup
import requests
import unittest
from datetime import datetime


class TestGetData(unittest.TestCase):
    def setUp(self):
        self.page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                                 headers={'User-Agent': 'Not blank'}).content
        self.soup = BeautifulSoup(self.page, 'lxml')
        self.hourly_data_output = get_hourly_data(self.soup, 'Aberdeen')
        self.keys = ['ozone', 'no2', 'so2', 'pm25', 'pm10', 'time']

    def test_hourly_data_1(self):
        self.assertEqual([type(a) for a in self.hourly_data_output.values()], [str] * 6)

    # test that last list item is a datetime string with the correct format
    def test_hourly_data_2(self):
        self.to_datetime = datetime.strptime(self.hourly_data_output['time'], '%d/%m/%Y %H:%M')
        self.assertIsInstance(self.to_datetime, datetime)

    # test that the list of values is returned unaltered if the site time is up-to-date
    def test_validate_data_1(self):
        self.mock_hourly_data = dict(zip(self.keys, ['46', '1', 'n/m', '3', '6'] + [datetime.strftime((datetime.now().
                                                                                                       replace(
            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M")]))
        self.assertEqual(validate_data(self.mock_hourly_data), self.mock_hourly_data)

    # test that sites with non up-to-date measurements (stale data) are handled correctly
    def test_validate_data_2(self):
        self.mock_hourly_data_2 = dict(zip(self.keys, ['46', '1', 'n/m', '3', '6'] + ['20/08/2017 10:00']))
        self.expected_output = dict(zip(self.keys, ['n/a'] * 5 + [datetime.strftime((datetime.now().replace(
            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M")]))
        self.assertEqual(validate_data(self.mock_hourly_data_2), self.expected_output)


if __name__ == '__main__':
    unittest.main()
