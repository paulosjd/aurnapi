from get_data import hourly_data, format_data
from bs4 import BeautifulSoup
from unittest import TestCase
import datetime

site_link_markdown1 = ''''''
data_row = """
[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">40 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">10 (1 Low)</span></td>,
 <td class="center"><span title="Not Measured">n/m</span></td>,
 <td class="center"><span class="bg_low1 bold">2 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)
 </span>
 </td>,
 <td>19/08/2017<br/>09:00:00</td>]
 """
site_link_markdown3 = """
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

##site_link_html = BeautifulSoup(data_row, 'html'))  soup from markdown i.e BeautifulSoup(site_link, 'html'))
##########################################See note below about format with datetime.now


class TestGetData(TestCase):

    def setUp(self):
        self.expected_get_data_output = ['39', '18', 'n/m', '6', '12', '19/08/2017 09:00:00']

    def test_hourly_data(self):
        self.html_input = BeautifulSoup(data_row, 'html')
        self.assertEqual(hourly_data(self.html_input), self.expected_get_data_output)

    #test that correct most up-to-date values are unaltered
    def test_format_data_1(self):
        self.assertEqual(format_data(self.expected_get_data_output), self.expected_get_data_output)

    #test that sites with non-up-to-date measurements are handled
    def test_format_data_3(self):
        self.data_list = ['39', '18', 'n/m', '6', '12', '19/08/2017 09:00:00']
        self.expected_output_1 = ['', '', '', '', '', '', '']
        self.expected_output_2 = ['', '', '', '', '', '', '']
        self.assertEqual()



row_soup = BeautifulSoup('''[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">39 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">18 (1 Low)</span></td>,
 <td class="center"><span title="Not Measured">n/m</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">12 (1 Low)
 </span>
 </td>,
 <td>14/08/2017<br/>16:00:00</td>]''', 'html.parser')


print(hourly_data('Aberdeen', row_soup.findAll('td')))



expected_list = ['Aberdeen', '39', '18', 'n/m', '6', '12', '14/08/2017 16:00:00']



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