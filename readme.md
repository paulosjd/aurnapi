A repository of the underlying code for the JSON API available at air-aware.com which was built using the Flask framework and 
the flask-SQLAlchemy extension. The API provides hourly-updated air quality data for 123 sites which form the UK's automatic monitoring network. Designed to be restful... Endpoints/routes, representation of data in JSON format. .. 

Contained within the directory named 'data' are modules which enable a database to be constructed and populated. The data is collected by parsing a webpage which is updated with recent air quality measurements on an hourly basis. Commands to scrape and insert data can be run manually but should ideally be setup to run automatically on a server. In order to run them in the Python interpreter, the application factory needs to be imported and then the application context pushed by running:

from app import create_app() 

create_app().app_context().push()

Run.py can be executed as a python file on a local machine...will access local database specified in config.py. 
include //localhost#;8080.  
to obtain list of sites and their site code which to search by...

information relating to the various monitoring sites can be obtained...


Air quaity data is filtered data according to a specified pollutant and monitoring site, as well as optional start and end dates 
e.g. http://localhost:8080/no2/ABD/2017-09-09/2017-09-12  
{
 "10/09/2017 00:00:00": "14",
  "10/09/2017 01:00:00": "17"
, "10/09/2017 02:00:00": "18"
,..etc..}


To test:   date filter work properly..e.g. what happen if enter...
                                  if just localhost.com/pm10  is empty qs??  
 					-just check that all designed endpoints work properly/as described
