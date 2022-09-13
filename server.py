from flask import Flask
app = Flask(__name__)
from weather import weather_by_city


@app.route("/")
def hello():
    return "Привет!"

if __name__=="__main__":
    weather = weather_by_city("Moscow,Russia")
    print(weather)
    app.run()