A REST API created to allow access to recent and historical air quality data via the website www.air-aware.com

Data on the website server is obtained by periodically scraping a government body webpage which updates every hour with the latest air quality measurements from sites in the UK's automatic monitoring network.


API endpoints
-------------

Endpoints are relative to the base URL: http://localhost:port and provide data in JSON format.
URLs are not case-sensitive


**/site-list**

'site code' and name of each monitoring site

**/data/{site code}/{previous days}**

data for a specified number of previous days and monitoring site


**/data/pollutants**

'pollutant' labels with full names and units of measurement


**/data/{site code}/{pollutant}/{previous days}**

data for a specified number of previous days, monitoring site and pollutant label


**/current-data/all-sites**

latest air quality data along with site information for each monitoring site

**/site-info/{site code}**

the name, region, environment type, official webpage URL, google maps URL, latitude and longitude for a specified site


Install
-------

Assuming Python 3.x and pip is installed, clone the repository and run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt






