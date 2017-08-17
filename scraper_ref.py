from site_metadata import site_urls, site_geo
from datetime import datetime
from app_ref import soup

#POTENTIAL CIRCULAR IMPORT WITH SOUP FROM APP_REF?


def get_data(site, soup):  #ASK MAL ABOUT SHADOW NAME SCOPING..
    site_link = soup.find_all('a', string=site)[0]
    site_row = site_link.findParent('td').findParent('tr')
    site_column = site_row.findAll('td')
    time_string = site_column[6].text
    time = time_string[:10] + ' ' + time_string[10:]
    o3 = site_column[1].text.replace('\xa0', ' ').split(' ')[0]
    no2 = site_column[2].text.replace('\xa0', ' ').split(' ')[0]
    so2 = site_column[3].text.replace('\xa0', ' ').split(' ')[0]
    pm25 = site_column[4].text.replace('\xa0', ' ').split(' ')[0]
    pm10 = site_column[5].text.replace('\xa0', ' ').split(' ')[0]
    site_values = [o3, no2, so2, pm25, pm10]
    """for value in site_values:
        if datetime.strptime(time, "%d/%m/%Y %H:%M:%S") != datetime.now().replace(microsecond=0, second=0, minute=0):

        else:
            value.replace('n/m', 'n/a')"""
    site_values = [value.replace(value, 'n/a') for value in site_values if datetime.strptime(time, "%d/%m/%Y %H:%M:%S")
                   != datetime.now().replace(microsecond=0, second=0, minute=0)]
    return [site, *site_values, time]






#test out the above with a mock list of site_values

##move the site_values reassignments to a function?
  ## - then can write a test for it
  ## - and comment for its purpose