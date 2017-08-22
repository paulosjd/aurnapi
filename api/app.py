from flask import Flask
from routes import get_pm10_blueprint

#engine = .....


app = Flask(__name__)
app.register_blueprint(get_pm10_blueprint)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080, passthrough_errors=True)
