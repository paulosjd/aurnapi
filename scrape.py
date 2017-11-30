from app.data.hourly import create_db, update_db
from app import create_app

create_app().app_context().push()
update_db()