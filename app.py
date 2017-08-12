from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:////tmp/aurn-api.db', convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import yourapplication.models
    Base.metadata.create_all(bind=engine)


class Sites(db.Model):
    __tablename__ = 'sites'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    url = db.Column(db.String(250))

    def __init__(self, name=None, url=None):
        self.name = name
        self.url = url

class Data(db.Model):
    __tablename__ = 'data'
    id = db.Column(db.Integer, primary_key=True)
    site = db.Column(db.String(100), db.ForeignKey('sites.name'))
    no2 = Column(Float(10))
    pm10 = Column(Float(10))
    pm25 = Column(Float(10))
    time = Column(String(50))

    def __init__(self, site=None, no2=None, pm10=None, pm25=None, time=None):
        self.site = site
        self.no2 = no2
        self.pm10 = pm10
        self.pm25 = pm25
        self.time = time


"""
db = MySQLdb.connect(host="localhost",
                     port=3306,
                     user="foo",
                     passwd="bar",
                     db="qoz")

cursor = db.cursor()


@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    try:
        cursor.execute("SELECT * FROM items")
        ...

    except:
        print "Error: unable to fetch items"
    return jsonify({"desired: " response})



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)

"""