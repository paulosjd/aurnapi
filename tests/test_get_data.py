from get_data import hourly_data, format_data
from bs4 import BeautifulSoup
import unittest
from datetime import datetime
"""

>>>print(hourly_data(soup, 'Aberdeen'))
['46', '1', 'n/m', '3', '6', '20/08/2017 10:00:00']

>>>print(format_data(hourly_data(soup, 'Aberdeen')))
['46', '1', 'n/m', '3', '6', '20/08/2017 10:00:00']

>>>foo = hourly_data(soup, 'Aberdeen')[0:5] + ['05/08/2017 14:00:00']
>>>print(foo)
['46', '1', 'n/m', '3', '6', '05/08/2017 14:00:00']
>>>print(format_data(foo))
['', '', '', '', '', '20/08/2017 11:00:00']
"""


class TestGetData(unittest.TestCase):
    def setUp(self):
        self.expected_get_data_output = ['39', '18', 'n/m', '6', '12', '19/08/2017 09:00:00']

    def test_hourly_data(self):
        self.html_input = BeautifulSoup(data_row, 'lxml')
        self.assertEqual(hourly_data(self.html_input), self.expected_get_data_output)

    # test that list is returned unaltered assuming that time is up-to-date
    def test_format_data_1(self):
        self.assertEqual(format_data(self.expected_get_data_output), self.expected_get_data_output)

    # test that sites with non-up-to-date measurements are handled
    def test_format_data_2(self):
        # noinspection PyTypeChecker,PyArgumentList
        self.expected_output = [''] * 5 + [datetime.strftime((datetime.now().replace(
            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
        self.assertEqual(format_data(self.expected_get_data_output), self.expected_output)

if __name__ == '__main__':
    unittest.main()

"""
mock_data =
[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">39 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">18 (1 Low)</span></td>,
 <td class="center"><span title="Not Measured">n/m</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">12 (1 Low)
 </span>
 </td>,
 <td>14/08/2017<br/>16:00:00</td>]
 """

"""
mock_data_wrong_time
[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">39 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">18 (1 Low)</span></td>,
 <td class="center"><span title="Not Measured">n/m</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">12 (1 Low)
 </span>
 </td>,
 <td>14/08/2017<br/>12:00:00</td>]
 """
