from flask import Flask
import sqlite3
from no2_scraper import no2_dict
#from pm_scraper import pm_dict

from sqlalchemy import create_engine


app = Flask(__name__)



engine = create_engine('sqlite:///aurn-api.db')


if __name__ == '__main__':
    initialize()
add_data()


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