Source code for the JSON API available at air-aware.com. It was  built using the Flask framework and the flask-SQLAlchemy extension. The API provides hourly-updated air quality data for 123 sites from the UK's automatic monitoring network. 

Contained within the directory named 'data' are modules which enable a database to be constructed and populated. The data is collected by parsing a webpage which is updated with recent air quality measurements on an hourly basis. Commands to scrape and insert data can be run manually but should ideally be setup to run automatically on a server. In order to run them in the Python interpreter, the application factory needs to be imported and then the application context pushed by running:

from app import create_app() 

create_app().app_context().push()

Run.py can be executed as a python file on a local machine...will access local database specified in config.py. 
include //localhost#;8080.  
to obtain list of sites and their site code which to search by...

information relating to the various monitoring sites can be obtained...


Air quaity data is filtered data according to a specified pollutant and monitoring site, as well as optional start and end dates 

Install
=========

Dependencies:

 - Python 3

   - https://www.python.org

 - PIP (Python package manager)

   - https://pypi.python.org/pypi/pip


Configure and run server:
------------------------

After cloning or downloading project files, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt

    python run.py

