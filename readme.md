A REST API created to allow access to recent and historical air quality data via the website www.air-aware.com

Data on the website server is obtained by periodically scraping a webpage which updates every hour with current air quality measurements from sites in the UK's automatic monitoring network.

# To do: mention SQLAlchemy as the ORM, how models linked via FK and how can access .. by e.g Site.Data.na....

API endpoints
-------------

Endpoints are relative to the base URL: http://localhost:port and provide data in JSON format.
URLs are not case-sensitive


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


Install
-------

Assuming Python 3.x and pip is installed, clone the repository and run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt


Create and populate database
----------------------------
The Flask application factory needs to be imported and the application context pushed by running:

    from app import create_app()

    create_app().app_context().push()

Create and populate a database using the create_db() and update_db() functions.

    from app.data.hourly import create_db, update_db

    create_db()

    update_db()

The create_db() function creates the table within a specified database. The 'sites' table will be prepopulated using values specified in app/data/site_info.py
The update_db() function runs the webscraping script and inserts the air quality data in the 'data' table


Configure and run the API
--------------------------
Once a populated database has been obtained and correct settings within app.config.py have been specified, run the following command within the project directory to make database queries:

    python run.py runserver




