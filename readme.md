An API for accessing air quality data, created for www.air-aware.com. The project was built using the Flask framework for Python, along with the flask-SQLAlchemy extension. 

Modules in app/data create and populate a database using data scraped from a webpage. This page is updated every hour with the latest air quality measurements for over 120 sites in the UK's automatic monitoring network.

The API gives access to the database. It follows REST design principles, providing data in JSON format through endpoints detailed as follows.


      
After cloning the repository, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt
    

Create and populate database
----------------------------
First, the Flask application factory needs to be imported and the application context pushed by running:

    from app import create_app()

    create_app().app_context().push()

Then, through Python, create and populate a database using the create_db() and update_db() functions in app/data/hourly.py

    >>> from app.data.hourly import create_db, update_db
    >>> create_db()
    >>> update_db()


Configure and run the API
--------------------------
Ensure correct settings within app/config.py and run the following command in the project directory:

    python run.py


API endpoints
-------------

Endpoints are relative to the base URL: http://localhost:5000
URLs are not case-sensitive


**/site-list**

'site code' labels used in api endpoints with the associated site name for each monitoring site


**/data/pollutants**

'pollutant' labels used in api endpoints with full names and units they are measured in
**/data/{pollutant}/{site code}**

hourly measurements and associated timepoints for a specified pollutant and monitoring site, e.g. /data/pm10/abd


**/data/{pollutant}/{site code}/{start date}**
**/data/{pollutant}/{site code}/{start date}/{end date}**

data filtered according to an optional start date (in format e.g. 2015-10-01)


**/available-data/{pollutant}/{site code}**

the starting date and number of available data points for a specified pollutant and monitoring site


**/site-regions**

a list of government regions within the AURN monitoring network


**/site-regions/{region}**

a list of names and site codes for all monitoring sites within a region, specified by writing as listed in /site-regions (e.g. /site-regions/greater-london)


**/site-environments/{environment-type}**

a list of names and site codes for all monitoring sites for an environment type, specified by writing as listed in /site-regions (e.g. /site-environments/urban-traffic)


**/site-geo**

geographical coordinates of all sites within the AURN network


**/site-url**

official webpage URL providing individual site information for all sites


**/site-maps**

google maps URLs for all sites 


**/site-info/{site code}**

the name, region, environment type, official webpage URL, google maps URL, latitude and longitude for a specified site

