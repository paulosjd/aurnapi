import requests
from bs4 import BeautifulSoup
from datetime import datetime
from site_lists import all_sites


page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')

ins = {'no2': no2_value}
no2_value = ''
data_dict = {site: ins for site in site_list}

site_column[2].text.replace('\xa0', ' ').split(' ')[0]
site_link = soup.find_all('a', string=site)[0]
site_row = site_link.findParent('td').findParent('tr')
site_column = site_row.findAll('td')
time_string = site_column[6].text
site_name = site_column[0].text
o3_value = site_column[1].text.replace('\xa0', ' ').split(' ')[0]
no2_value = site_column[2].text.replace('\xa0', ' ').split(' ')[0]
so2_value = site_column[3].text.replace('\xa0', ' ').split(' ')[0]
pm25_value = site_column[4].text.replace('\xa0', ' ').split(' ')[0]
pm10_value = site_column[5].text.replace('\xa0', ' ').split(' ')[0]
if no2_value == 'n/a':
    no2_value = ''
ins.update({'no2': no2_value})


