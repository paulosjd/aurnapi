from flask import Flask
from flask_migrate import Manager, Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app/database.db'

db = SQLAlchemy(app)

with app.app_context():
    # Import models even though they are not used, otherwise Alembic will not detect them
    from app.models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
