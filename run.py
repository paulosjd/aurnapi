from app import create_app
from flask_migrate import Manager, Migrate, MigrateCommand
from app.models import db

app = create_app()

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

manager.run()
