import sys
from app import create_app
from app.models import db, Site
from app.data.site_info import get_info, site_list

application = create_app()


if __name__ == '__main__':
    if "createdb" in sys.argv:
        with application.app_context():
            db.create_all()
        print("Database created!")
    elif "addsites" in sys.argv:
        with application.app_context():
            for site in site_list:
                site_info = Site(**get_info(site))
                db.session.add(site_info)
            db.session.commit()
            print("Site table populated")
    else:
        application.run(debug=True)