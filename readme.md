An API for air quality data created for air-aware.com. The project was built using the Flask framework for Python, along with the flask-SQLAlchemy extension. 

Modules in app/data create and populate a database using data obtained by parsing a webpage. This page is updated with air quality measurements on an hourly basis with data for over 120 sites within the UK's automatic monitoring network.

The API allows access to air quality data in JSON format through endpoints detailed in app/views. These incldue:

Site poll, site 
/uri/<poll>....
                /<start_date>
		/ ............/<end_date>
Optional start and end dates can be specified.

Pollutant data of interest along with the individual monitoring sites must be specied. The pollutant names and monitoring site codes are avaiable at:
/uri/site-list
/uri/pollutants  codes e.g. 'no2' which refer to the pollutant name and measurement unit e.g. 'nitrogen dioxide, ppm'


'ozone': 'ozone, ppm', ',  'no2': 'nitrogen dioxide, ppm', 'pm10    NEED TO MAKE!!



Install
-------

Dependencies:

 - Python 3

   - https://www.python.org

 - PIP (Python package manager)

   - https://pypi.python.org/pypi/pip
   
   
After cloning the repository, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt
    

Create and populate database
----------------------------
Before running commands in a Python interpreter, the Flask application factory needs to be imported and the application context pushed by running:

    from app import create_app()

    create_app().app_context().push()


Create and populate a database using the create_db() and update_db() functions within app/data/hourly.py  


Configure and run the API:
--------------------------
Once a populated database has been obtained and correct settings within app.config.py have been specified, run the following command to run queries using the endpoints specified in the views directory:

    python run.py
