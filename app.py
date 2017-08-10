from flask import Flask
import _mysql

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", "yourDbPassWord", "DBname")

def connection():
    conn = MySQLdb.connect(host="localhost",
                           user = "root",
                           passwd = "cookies!",
                           db = "pythonprogramming")
    c = conn.cursor()

    return c, conn

@app.route('/api/v1.0/items', methods=['GET'])
def get_items():
    curs = db.cursor()
    try:
        curs.execute("SELECT * FROM items")
        ...

    except:
        print "Error: unable to fetch items"
    return jsonify({"desired: " response})


#db.query("""SELECT spam, eggs, sausage FROM breakfast
 #        WHERE price < 5""")

#r=db.store_result()

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)