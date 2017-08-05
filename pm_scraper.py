import requests
from bs4 import BeautifulSoup

#execute daily using CRON  - daily running 24 hour means


url = 'https://uk-air.defra.gov.uk/latest/currentlevels'

defra_page = requests.get(url)
soup = BeautifulSoup(defra_page, 'html.parser')


#if latest value .... else ''
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
'Middlesborough',
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
'Barnstaple',
"Bristol St Paul's",
'Plymouth Centre',
'Birmingham A4540 Roadside',
'Coventry Binley Road',
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



































