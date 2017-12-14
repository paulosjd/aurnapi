A REST API created to serve as a convenient means for accessing air quality data. With Python, the requests library and a JavaScript charting library, time series graphs can easily be created to show recent levels and historical trends etc.

The file app/data/hourly.py populates a database by scraping a government body webpage which shows the most recent hourly air quality measurements from sites in the UK's automatic monitoring network.

The project was built using Flask web framework for Python along with Flask-SQLAlchemy as the ORM. The files which serve the API endpoints through database queries are contained within app/views.

API endpoints
-------------

Endpoints provide data in JSON format and are not case-sensitive


**/site-list**

'site code' and name of each monitoring site

**/data/{site code}/{days}**

data for a specified number of previous days and monitoring site


**/data/{site code 1}/{site code 2}/{days}**

data from two monitoring sites for a number of previous days


**/data/pollutants**

'pollutant' labels with full names and units of measurement


**/data/{site code}/{pollutant}/{days}**

data for a specified number of previous days, monitoring site and pollutant label


**/current-data/all-sites**

latest air quality data along with site information for each monitoring site

**/site-info/{site code}**

the site name, region, environment type, latitude, longitude and official webpage URL for additional site information


Getting Started
---------------
**Prerequisites**

Python 3.4

pip

virtualenv

**1. Clone or copy repository**

**2. Set up Virtual Environment**

Create a virtual environment named aurn-venv:

    $ virtualenv aurn-venv

Activate the virtual environment:

    $ source aurn-venv/bin/activate
    (aurn-venv) $

Use *pip* to install requirements:

    (aurn-venv) $ pip install requirements.txt

Verify that packages have been installed:

    (aurn-venv) $ pip freeze
    Flask==0.12
    Flask_SQLAlchemy==2.1
    pytz==2017.2
    flask-migrate==2.1.1
    requests==2.13.0
    beautifulsoup4==4.6.0

**3. Push Flask application context**

Run the following commands in Python within the virtual environment:

    >>> from app import create_app()

    >>> create_app().app_context().push()


Create and populate a database using the create_db() and update_db() functions.

    >>> from app.data.hourly import create_db, update_db

    >>> create_db()

    >>> update_db()

The create_db() function creates the database schema. The update_db() function runs the webscraping script and inserts the air quality data in the 'data' table. This should be set up to run on an hourly basis; n.b. the webpage https://uk-air.defra.gov.uk/latest/currentlevels updates at 40 minutes past the hour.


**4. Configure and run the API**

After ensuring correct settings within app/config, the database can be queried through the API after running the server:

    $ python run.py




