A REST API created to serve as a convenient means for accessing air quality data. With Python, the requests library and a JavaScript charting library, time series graphs can easily be created to show recent levels and historical trends etc. Examples are found at: www.air-aware.com/charts.

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


Install
-------

Clone this repo to your local machine. In the top level directory, create a virtual environment:

    $ virtualenv flask-aws
    $ source flask-aws/bin/activate
    -see example http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html

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
After ensuring correct settings within app/config, the populated database can be queried by running the following command in the project directory:

    python run.py




