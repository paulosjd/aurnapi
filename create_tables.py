from flask import Flask
from models import db, Sites
from site_metadata import site_list, get_info


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db.init_app(app)

def create_database():
    with app.app_context():
        db.create_all()

        for site in site_list:  # only want to run once, not every time with data by CRON
            site_info = Sites(*get_info(site))
            db.session.add(site_info)

        db.session.commit()
