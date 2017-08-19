from get_data import hourly_data
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

    def test_get_data(self):
        self.hourly_data = BeautifulSoup(data_row, 'html')
        self.make_list =
        self.expected_list = ['Aberdeen', '39', '18', 'n/m', '6', '12', '19/08/2017 09:00:00']
        self.assertEqual(self.hourly_data, self.expected_list)

    def test_format_data(self):
        self.expected_list=
        self.assertEqual()

    def test_hourly_data_markdown3(self):
        self.expected_list= ['Aberdeen', '', '', 'n/m', '', '', datetime.now().replace(
        microsecond=0, second=0, minute=0)]
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