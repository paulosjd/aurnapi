from datetime import datetime


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


"""

#page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
#soup = BeautifulSoup(page, 'lxml')
#print(hourly_data(soup, 'Aberdeen'))
#print(format_data(hourly_data(soup, 'Aberdeen')))

>>>print(hourly_data(soup, 'Aberdeen'))
['46', '1', 'n/m', '3', '6', '20/08/2017 10:00:00']

>>>print(format_data(hourly_data(soup, 'Aberdeen')))
['46', '1', 'n/m', '3', '6', '20/08/2017 10
:00:00']

>>>foo = hourly_data(soup, 'Aberdeen')[0:5] + ['05/08/2017 14:00:00']
>>>print(foo)
['46', '1', 'n/m', '3', '6', '05/08/2017 14:00:00']
>>>print(format_data(foo))
['', '', '', '', '', '20/08/2017 11:00:00']
"""