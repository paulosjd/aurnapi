The application collects and stores recent and historical air pollution measurements from sites within an automated monitoring network.
REST API supports basic HTTP methods and the data is consumed by a React [demo app](https://ukair.paulja.me/) .
 
Requirements include Flask, Flask-Login, Flask-SQLAlchemy and [Marshmallow](http://marshmallow.readthedocs.io/). 
Swagger UI documentation is generated from .yml files using [Flasgger](https://github.com/rochacbruno/flasgger).  

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
    beautifulsoup4==4.6.0
    Flask==0.12
    Flask_Login==0.4.0
    flask_marshmallow==0.8.0
    Flask_SQLAlchemy==2.1
    flasgger==0.8.1
    marshmallow==2.14.0
    pytz==2017.3
    requests==2.13.0


**3. Create the database and add data**

    (aurn-venv) $ python3 run.py createdb

    (aurn-venv) $ python3 run.py collectdata

The collectdata command provides a convenient way to update the database with air pollution values scraped from the goverment agency webpage, updated on an hourly basis.  

**4. Configure and run the API**

After ensuring correct settings, the resources can be accessed through the API after running the server:

    $ python run.py
