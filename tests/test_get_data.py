from get_data import hourly_data, format_data
from bs4 import BeautifulSoup
import requests
import unittest
from datetime import datetime


class TestGetData(unittest.TestCase):

    def setUp(self):
        self.page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                                 headers={'User-Agent': 'Not blank'}).content
        self.soup = BeautifulSoup(self.page, 'lxml')
        self.hourly_data_output = hourly_data(self.soup, 'Aberdeen')

    def test_hourly_data_1(self):
        self.list_item_types = [type(a) for a in self.hourly_data_output]
        self.assertEquals(self.list_item_types, [str] * 6)

        # test that last list item [5] is a datetime string with the correct format
    def test_hourly_data_2(self):
        self.to_datetime = datetime.strptime(self.hourly_data_output[5], '%d/%m/%Y %H:%M:%S')
        self.assertIsInstance(self.to_datetime, datetime)
        
        # test that list is returned unaltered if time is up-to-date
    def test_format_data_1(self):
        self.get_data_output_1 = ['46', '1', 'n/m', '3', '6'] + [datetime.strftime((datetime.now().replace(
            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
        self.assertEqual(format_data(self.get_data_output_1), self.get_data_output_1)

        # test that sites with non-up-to-date measurements are handled correctly
    def test_format_data_2(self):
        self.get_data_output_1 = ['46', '1', 'n/m', '3', '6', '20/08/2017 10:00:00']
        self.expected_output_2 = [''] * 5 + [datetime.strftime((datetime.now().replace(
            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
        self.assertEqual(format_data(self.get_data_output_1), self.expected_output_2)


if __name__ == '__main__':
    unittest.main()
