An API for air quality data created for air-aware.com. The project was built using the Flask framework for Python, along with the flask-SQLAlchemy extension. 

Modules in app/data create and populate a database using data obtained by parsing a webpage. This page is updated with air quality measurements on an hourly basis with data for over 120 sites within the UK's automatic monitoring network.

The API allows access to air quality data in JSON format through endpoints detailed as follows.

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


Configure and run the API
--------------------------
Once a populated database has been obtained and correct settings within app.config.py have been specified, run the following command to run queries using the endpoints specified in the views directory:

    python run.py

API endpoints
-------------
