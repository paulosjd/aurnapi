import requests
from bs4 import BeautifulSoup
from datetime import datetime


url = 'https://uk-air.defra.gov.uk/latest/currentlevels'

defra_page = requests.get(url)
soup = BeautifulSoup(defra_page, 'html.parser')

site_list = [
    'Edinburgh St Leonards',
    'Glasgow High Street',
    'Grangemouth',
    'Grangemouth Moray',
    'Chesterfield Loundsley Green',
    'Chesterfield Roadside',
    "Derby St Alkmund's Way",
    'Ladybower',
    'Leicester A594 Roadside',
    'Leicester University',
    'Nottingham Centre',
    'Nottingham Western Boulevard',
    'Cambridge Roadside',
    'Luton A505 Roadside',
    'Norwich Lakenfields',
    'Sandy Roadside',
    'Southend-on-Sea',
    'St Osyth',
    'Stanford-le-Hope Roadside',
    'Thurrock',
    'Wicken Fen',
    'Camden Kerbside',
    'London Bexley',
    'London Bloomsbury',
    'London Eltham',
    'London Harlington',
    'London Marylebone Road',
    'London N. Kensington',
    'London Westminster',
    'Fort William',
    'Inverness',
    'Middlesbrough',
    'Newcastle Centre',
    'Stockton-on-Tees Eaglescliffe',
    'Sunderland Silksworth',
    'Sunderland Wessington Way',
    'Aberdeen',
    'Aberdeen Union Street Roadside',
    'Aberdeen Wellington Road',
    'Aston Hill',
    'Wrexham',
    'Birkenhead Borough Road',
    'Blackpool Marton',
    'Bury Whitefield Roadside',
    'Carlisle Roadside',
    'Glazebury',
    'Liverpool Speke',
    'Manchester Piccadilly',
    'Manchester Sharston',
    'Preston',
    'Salford Eccles',
    'Shaw Crompton Way',
    'St Helens Linkway',
    'Warrington',
    'Widnes Milton Road',
    'Wigan Centre',
    'Wirral Tranmere',
    'Armagh Roadside',
    'Belfast Centre',
    "Belfast Stockman's Lane",
    'Eskdalemuir',
    'Peebles',
    'Brighton Preston Park',
    'Canterbury',
    'Chatham Roadside',
    'Chilbolton Observatory',
    'Eastbourne',
    'Horley',
    'Lullington Heath',
    'Oxford Centre Roadside',
    'Oxford St Ebbes',
    'Portsmouth',
    'Reading London Road',
    'Reading New Town',
    'Rochester Stoke',
    'Southampton A33',
    'Southampton Centre',
    'Worthing A27 Roadside',
    'Cardiff Centre',
    'Chepstow A48',
    'Cwmbran',
    'Narberth',
    'Newport',
    'Port Talbot Margam',
    'Swansea Roadside',
    'Bath Roadside',
    'Bournemouth',
    "Bristol St Paul's",
    'Bristol Temple Way',
    'Charlton Mackrell',
    'Christchurch Barrack Road',
    'Exeter Roadside',
    'Plymouth Centre',
    'Plymouth Tavistock Road.',
    'Yarner Wood',
    'Birmingham A4540 Roadside',
    'Birmingham Acocks Green',
    'Cannock A5190 Roadside',
    'Coventry Allesley',
    'Coventry Binley Road.',
    'Leamington Spa',
    'Leamington Spa Rugby Road',
    'Leominster',
    'Oldbury Birmingham Road',
    'Stoke-on-Trent A50 Roadside',
    'Stoke-on-Trent Centre',
    'Walsall Woodlands',
    'Barnsley Gawber',
    'Bradford Mayo Avenue',
    'Doncaster A630 Cleveland Street',
    'High Muffles',
    'Hull Freetown',
    'Hull Holderness Road',
    'Leeds Centre',
    'Leeds Headingley Kerbside',
    'Scunthorpe Town',
    'Sheffield Barnsley Road',
    'Sheffield Devonshire Green',
    'Sheffield Tinsley',
    'York Bootham',
    'York Fishergate'
]

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = bs4.BeautifulSoup(page, 'lxml')

no2_value = ''
data_dict = {site:no2_value for site in site_list}
last_hour = (datetime.now().replace(microsecond=0,second=0,minute=0))
for site in site_list:
    site_link = soup.find_all('a',string=site)[0]
    site_row = site_link.findParent('td').findParent('tr')
    site_column = site_row.findAll('td')
    time_string = site_column[6].text
    site_name = site_column[0].text
    no2_value = {site:site_column[2].text}
    #if 'condition':
        #data_dict.update(no2_value)


for site in site_list:
    print (soup.find_all('a',string=site)[0].text)
    
   
for site in site_list:
    #site_link = soup.find_all('a',string=site)[0]
    #site_row = site_link.findParent('td').findParent('tr')
    no2_value = site_row.findAll('td')[2].text
    
for site in site_list:
    #site_link = soup.find_all('a',string=site)[0]
    #site_row = site_link.findParent('td').findParent('tr')
    time = site_row[6].text

