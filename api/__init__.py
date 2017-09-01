from flask import Flask
from flask_sqlalchemy import SQLAlchemy


##look at application factories

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)
