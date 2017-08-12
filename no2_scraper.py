import requests
from bs4 import BeautifulSoup
from datetime import datetime
from site_lists import no2_site_list

#execute hourly using CRON


page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = BeautifulSoup(page, 'lxml')


no2_dict = {site_name:{'no2': no2_value}}, time

for site in no2_site_list}site_link = soup.find_all('a',string=site)[0]:
    site_row = site_link.findParent('td').findParent('tr')
    site_column = site_row.findAll('td')
    time = site_column[6].text
    site_name = site_column[0].text
    no2_value = site_column[2].text.replace('\xa0', ' ').split(' ')[0]
    if no2_value == 'n/a':
        no2_value = ''


print(no2_dict)



"""

page = requests.get('https://uk-air.defra.gov.uk/latest/currentlevels', headers={'User-Agent': 'Not blank'}).content
soup = bs4.BeautifulSoup(page, 'lxml')
Edinburgh_link = soup.find_all('a',string='Edinburgh St Leonards')[0]
#>>>Edinburgh_link.text
#'Edinburgh St Leonards'
Edinburgh_row = Edinburgh_link.findParent('td').findParent('tr')
Edinburgh_columns = Edinburgh_row.findAll('td')
Edinburgh_columns[2].text
#cell for hourly mean NO2 for
dt = Edinburgh_columns[6].text
time = datetime.strptime(dt , '%d/%m/%Y%H:%M:%S')
last_hour = (datetime.now().replace(microsecond=0,second=0,minute=0))
#datetime.strptime(mystring, "%d/%m/%Y%H:%M:%S")

for site in no2_site_list:
    print (soup.find_all('a',string=site)[0].text)

#for site in no2_site_list:
site = no2_site_list[0]
# if soup.find .type() == float and datetime == most recent data
value = soup.find(....)
# else:
#value = ''


'Edinburgh St Leonards'
'Glasgow High Street'
'Grangemouth'
'Grangemouth Moray'
'Chesterfield Loundsley Green'
'Chesterfield Roadside'
"Derby St Alkmund's Way"
'Ladybower'
'Leicester A594 Roadside'
'Leicester University'
'Nottingham Centre'
'Nottingham Western Boulevard'
'Cambridge Roadside'
'Luton A505 Roadside'
'Norwich Lakenfields'
'Sandy Roadside'
'Southend-on-Sea'
'St Osyth'
'Stanford-le-Hope Roadside'
'Thurrock'
'Wicken Fen'
'Camden Kerbside'
'London Bexley'
'London Bloomsbury'
'London Eltham'
'London Harlington'
'London Marylebone Road'
'London N. Kensington'
'London Westminster'
'Fort William'
'Inverness'
'Middlesborough'
'Newcastle Centre'
'Stockton-on-Tees Eaglescliffe'
'Sunderland Silksworth'
'Sunderland Wessington Way'
'Aberdeen'
'Aberdeen Union Street Roadside'
'Aberdeen Wellington Road'
'Aston Hill'
'Wrexham'
'Birkenhead Borough Road'
'Blackpool Marton'
'Bury Whitefield Roadside'
'Carlisle Roadside'
'Glazebury'
'Liverpool Speke'
'Manchester Piccadilly'
'Manchester Sharston'
'Preston'
'Salford Eccles'
'Shaw Compton Way'
'St Helens Linkway'
'Warrington'
'Widnes Milton Road'
'Wigan Centre'
'Wirral Tranmere'
'Armagh Roadside'
'Belfast Centre'
"Belfast Stockman's Lane"
'Eskdalemuir'
'Peebles'
'Brighton Preston Park'
'Canterbury'
'Chatham Roadside'
'Chilbolton Observatory'
'Eastbourne'
'Horley'
'Lullington Heath'
'Oxford Centre Roadside'
'Oxford St Ebbes'
'Portsmouth'
'Reading London Road'
'Reading New Town'
'Rochester Stoke'
'Southamptom A33'
'Southampton Centre'
'Worthing A27 Roadside'
'Cardiff Centre'
'Chepstow A48'
'Cwmbran'
'Narberth'
'Newport'
'Port Talbot Margam'
'Swansea Roadside'
'Bath Roadside'
'Bournemouth'
"Bristol St Paul's"
'Bristol Temple Way'
'Charlton Mackrell'
'Christchurch Barrack Road'
'Exeter Roadside'
'Plymouth Centre'
'Plymouth Tavistock Road'
'Yarner Wood'
'Birmingham A4540 Roadside'
'Birmingham Acocks Green'
'Cannock A5190 Roadside'
'Coventry Allesley'
'Coventry Binley Road'
'Leamington Spa'
'Leamington Spa Rugby Road'
'Leominster'
'Oldbury Birmingham Road'
'Stoke-on-Trent A50 Roadside'
'Stoke-on-Trent Centre'
'Walsall Woodlands'
'Barnsley Gawber'
'Bradford Mayo Avenue'
'Doncaster A630 Cleveland Street'
'High Muffles'
'Hull Freetown'
'Hull Holderness Road'
'Leeds Centre'
'Leeds Headingley Kerbside'
'Scunthorpe Town'
'Sheffield Barnsley Road'
'Sheffield Devonshire Green'
'Sheffield Tinsley'
'York Bootham'
'York Fishergate'
"""


































