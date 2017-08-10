from flask import Flask
import MySQLdb

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", "yourDbPassWord", "DBname")



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)