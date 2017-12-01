An API for accessing air quality data, created for www.air-aware.com. The project was built using the Flask framework for Python, along with the flask-SQLAlchemy extension. 

Modules in app/data create and populate a database using data scraped from a webpage. This page is updated every hour with the latest air quality measurements for over 120 sites in the UK's automatic monitoring network.

The API gives access to the database. It follows REST design principles, providing data in JSON format through endpoints detailed as follows.


      
After cloning the repository, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt
    

Create and populate database
----------------------------
Before running commands in a Python interpreter, the Flask application factory needs to be imported and the application context pushed by running:

    from app import create_app()

    create_app().app_context().push()

Create and populate a database using the create_db() and update_db() functions within app/data/hourly.py  


Configure and run the API
--------------------------
Once a populated database has been obtained and correct settings within app.config.py have been specified, run the following command within the project directory to make database queries:

    python run.py runserver


API endpoints
-------------

Endpoints are relative to the base URL: http://localhost:5000


**/site-list**

a list of names and site codes for all 123 monitoring sites 


**/data/pollutants**

a list of air quality parameters for which data is available, the units they are measured in, and their ‘url labels’ required for accessing the following the endpoints

**/data/{pollutant}/{site code}**

a list of hourly measurements and associated timepoints for a specified pollutant and monitoring site, e.g. /data/pm10/abd


**/data/{pollutant}/{site code}/{start date}**
data filtered according to an optional start and end date (in format e.g. 2015-10-01)


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

