Source code for the JSON API available at air-aware.com. It was  built using the Flask framework and the flask-SQLAlchemy extension. The API provides hourly-updated air quality data for 123 sites from the UK's automatic monitoring network. 

Modules within the 'data' directory enable a database to be constructed and populated. The data is collected by parsing a webpage which is updated with recent air quality measurements on an hourly basis. Running update_db() should be carried out shortly before the hour rather than after, e.g. 14:55 rather than 15:05

Commands to scrape and insert data can be run manually but ideally should be setup to run automatically on a server. In order to run them in the Python interpreter, the application factory needs to be imported and then the application context pushed by running:

from app import create_app() 

create_app().app_context().push()

Run.py can be executed as a python file on a local machine, allowing the database specified in config.py to be queried through entering certain endpoints. The endpoints include list of sites and their site code with which to search by, as welll as information relating to the various monitoring sites. Endpoints for air quality data return data which is filtered data according to the specified pollutant and monitoring site, as well as optional start and end dates. 



Configure and run the API:
--------------------------

After downloading project files and populating the database, run the following commands from the project's root directory:

    pip install --upgrade pip

    pip install -r requirements.txt

    python run.py

