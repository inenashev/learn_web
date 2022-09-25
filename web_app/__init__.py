from flask import Flask, render_template
from web_app.weather import weather_by_city
from web_app.python_org_news import get_python_news

def create_app():

    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('config.py')

    @app.route('/')
    def index():
        page_title = 'новости python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = get_python_news()
        return render_template("index.html", page_title = page_title, weather=weather, news_list = news_list)

    return app