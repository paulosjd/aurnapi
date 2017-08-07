import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://uk-air.defra.gov.uk/latest/currentlevels'

defra_page = requests.get(url)
soup = BeautifulSoup(defra_page, 'html.parser')

site_list = [
'Auchencorth Moss',
'Edinburgh St Leonards',
'Glasgow High Street',
'Grangemouth',
'Chesterfield Loundsley Green',
'Chesterfield Roadside',
'Leicester A594 Roadside',
'Leicester University',
'Nottingham Centre',
'Nottingham Western Boulevard',
'Norwich Lakenfields',
'Southend-on-Sea',
'Thurrock',
'Camden Kerbside',
'London Bexley',
'London Bloomsbury',
'London Marylebone Road',
'London N. Kensington',
'Middlesbrough',
'Newcastle Centre',
'Stockton-on-Tees Eaglescliffe',
'Sunderland Silksworth',
'Blackpool Marton',
'Bury Whitefield Roadside',
'Carlisle Roadside',
'Liverpool Speke',
'Manchester Piccadilly',
'Preston',
'Salford Eccles',
'St Helens Linkway',
'Warrington',
'Wigan Centre',
'Wirral Tranmere',
'Armagh Roadside',
'Belfast Centre',
"Belfast Stockman's Lane",
'Chatham Roadside',
'Chilbolton Observatory',
'Eastbourne',
'Oxford St Ebbes',
'Portsmouth',
'Reading London Road',
'Reading New Town',
'Rochester Stoke',
'Southamptom A33',
'Southampton Centre',
'Cardiff Centre',
'Chepstow A48',
'Port Talbot Margam',
'Barnstaple A39',
"Bristol St Paul's",
'Plymouth Centre',
'Birmingham A4540 Roadside',
'Coventry Binley Road.',
'Leamington Spa',
'Leamington Spa Rugby Road',
'Stoke-on-Trent A50 Roadside',
'Stoke-on-Trent Centre',
'Hull Freetown',
'Hull Holderness Road',
'Leeds Centre',
'Leeds Headingley Kerbside',
'Scunthorpe Town',
'Sheffield Devonshire Green',
'York Bootham',
'York Fishergate'
]

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = bs4.BeautifulSoup(page, 'lxml')
time = datetime.strptime(dt , '%d/%m/%Y%H:%M:%S')
last_hour = (datetime.now().replace(microsecond=0,second=0,minute=0))

for site in site_list:
    print (soup.find_all('a',string=site)[0].text)
 
for site in site_list:
    site_link = soup.find_all('a',string=site)[0]
    site_row = site_link.findParent('td').findParent('tr')
    latest_times = site_row.findAll('td')[6].text
 
#running 24hour mean pm2.5:
site_row.findAll('td')[4].text

#running 24hour mean pm10:
site_row.findAll('td')[5].text
