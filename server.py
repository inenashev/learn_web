from flask import Flask
app = Flask(__name__)
from weather import weather_by_city


@app.route('/')
def index():
    weather = weather_by_city("Moscow,Russia")
    if weather:
        return f"Сейчас {weather['temp_C']},ощущается как {weather['FeelsLikeC']}"
    else:
        return "Прогноз сейчас недоступен"

if __name__=="__main__":
    #weather = weather_by_city("Moscow,Russia")
    #print(weather)
    app.run()