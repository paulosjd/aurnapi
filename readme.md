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

All data is hourly measurements of air quality parameters from aurn- automatic monitoring


**/site-list**

'site code' and name for each monitoring site

**/data/{site code}/{previous days}**

data for a specified number of previous days and monitoring site


**/data/pollutants**

'pollutant' labels with full names and units of measurement


**/data/{site code}/{pollutant}/{previous days}**

data for a specified number of previous days, monitoring site and pollutant label



**/site-info/{site code}**

the name, region, environment type, official webpage URL, google maps URL, latitude and longitude for a specified site

