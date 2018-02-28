import sys
from app import create_app
from app.data.sites import create_db
from app.data.hourly import update_db

application = create_app()


if __name__ == '__main__':
    if "createdb" in sys.argv:
        with application.app_context():
            create_db()
    elif "collectdata" in sys.argv:
        with application.app_context():
            update_db()
    else:
        application.run(debug=True)