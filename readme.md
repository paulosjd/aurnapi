A prototype API for hourly mean air pollution data obtained by periodic scraping of a government agency webpage.
 
The API serves data in JSON format and supports basic HTTP methods and CRUD operations. It was built using Flask, Flask-Login, Flask-SQLAlchemy and Marshmallow. Swagger UI documentation is generated using Flasgger (http://127.0.0.1:5000/apidocs/).



Getting Started
---------------


**Prerequisites**

Python 3.4, pip, virtualenv

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
    Flask_Login==0.4.0
    flask_marshmallow==0.8.0
    Flask_SQLAlchemy==2.1
    flasgger==0.8.1
    marshmallow==2.14.0
    marshmallow-sqlalchemy==0.13.2
    pytz==2017.3
    requests==2.13.0
    beautifulsoup4==4.6.0

**3. Create the database and add data**


    (aurn-venv) $ python3 run.py createdb

    (aurn-venv) $ python3 run.py collectdata

The collectdata command provides a convenient way to call the update_db() function (defined in app.data.hourly). This inserts the air quality data for the most recent hour into the table 'data'. 


**4. Configure and run the API**

After ensuring correct settings, the resources can be accessed through the API after running the server:

    $ python run.py
