import requests
from bs4 import BeautifulSoup

#execute daily using CRON  - daily running 24 hour means


url = 'https://uk-air.defra.gov.uk/latest/currentlevels'

defra_page = requests.get(url)
soup = BeautifulSoup(defra_page, 'html.parser')

