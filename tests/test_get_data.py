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

    def test_hourly_data_1(self):
        ####test that is list containing 6 strings with last item being date time string/match expected format
        self.output = hourly_data(self.soup, 'Aberdeen')
        ###self.assert......(hourly_data(self.soup, 'Aberdeen'), )
        ####self.assertIs([str*6]

        # test that list item [5] regex date time string matches
    def test_hourly_data_2(self):
        self.page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels',
                                 headers={'User-Agent': 'Not blank'}).content
        self.soup = BeautifulSoup(self.page, 'lxml')
        self.output = hourly_data(self.soup, 'Aberdeen')
        ####test that is list item [5] regex date time string matches
        ###self.assert......(hourly_data(self.soup, 'Aberdeen'), )
        self.assertRegexpMatches

        # test that list is returned unaltered assuming that time is up-to-date
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
