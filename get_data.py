from datetime import datetime
from site_metadata import site_geo, site_urls
from bs4 import BeautifulSoup
import requests


row = """[<td><a href="../networks/site-info?site_id=ABD">Aberdeen</a><br/>
 <a class="smalltext" href="https://uk-air.defra.gov.uk/assets/graphs/ABD_weekly_m.png">Timeseries Graph</a></td>,
 <td class="center"><span class="bg_low2 bold">48 (2 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">4 (1 Low)</span></td>,
 <td class="center"><span title="Not Measured">n/m</span></td>,
 <td class="center"><span class="bg_low1 bold">2 (1 Low)</span></td>,
 <td class="center"><span class="bg_low1 bold">6 (1 Low)
 </span>
 </td>,
 <td>19/08/2017<br/>17:00:00</td>]"""

def hourly_data(soup, site):
    site_link = soup.find_all('a', string=site)[0]
    row = site_link.findParent('td').findParent('tr').findAll('td')
    o3 = row[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = row[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = row[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = row[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = row[5].text.replace('\xa0', ' ').split(' ')[0]
    time = row[6].text[:10] + ' ' + row[6].text[10:]
    return [o3, no2, so2, pm25, pm10, time]


def format_data(hourly_data_output):
    if hourly_data_output[5] != datetime.strftime((datetime.now().replace(microsecond=0, second=0, minute=0)),
                                                   "%d/%m/%Y %H:%M:%S"):
        return [''] * 5 + [datetime.strftime((datetime.now().replace(
                                                            microsecond=0, second=0, minute=0)), "%d/%m/%Y %H:%M:%S")]
    else:
        return hourly_data_output


def get_info(site):
    url = site_urls.get(site)
    lat = site_geo.get(site)[0]
    long = site_geo.get(site)[1]
    return [site, url, lat, long]


page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')
#print(hourly_data(soup, 'Aberdeen'))
#print(format_data(hourly_data(soup, 'Aberdeen')))

foo = hourly_data(soup, 'Aberdeen')[0:5] + ['05/08/2017 14:00:00']
print(format_data(foo))
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
