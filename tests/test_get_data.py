from get_data import hourly_data
from bs4 import BeautifulSoup
from unittest import TestCase

site_link markdown1 = ''''''
site_link markdown2 = """
mock_data =
[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">39 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">18 (1 Low)</span></td>,
 <td class="center"><span title="bg_low1 bold">18</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">12 (1 Low)
 </span>
 </td>,
 <td>14/08/2017<br/>16:00:00</td>]
 """
site_link markdown3 = """
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

##site_link_html = BeautifulSoup(site_link_html, 'html'))  soup from markdown i.e BeautifulSoup(site_link, 'html'))
##########################################See note below about format with datetime.now


class TestGetData(TestCase):

    def setUp(self):
        #self.entry with correct time etc = BeautifulSoup(site_link markdown1, 'html')
        #self.entry with incorrect time = BeautifulSoup(site_link markdown2, 'html')
        # self.entry with 'n/m' and incorrect time = BeautifulSoup(site_link markdown3, 'html')


    def test_hourly_data_markdown1(self):
        self.hourly_data(site_link_html.findParent('td').findParent('tr').findAll('td'))
        #format the above with datetime.now()..replace???
        self.expected_list = ['Aberdeen', '39', '18', 'n/m', '6', '12', datetime.now().replace(
        microsecond=0, second=0, minute=0)]
        self.assertEqual(self.hourly_data, self.expected_list)

    def test_hourly_data_markdown2(self):
        self.expected_list= ['Aberdeen', '', '', '', '', '', datetime.now().replace(
        microsecond=0, second=0, minute=0)]
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