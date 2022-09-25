from flask import Flask, render_template
from web_app.weather import weather_by_city
from web_app.python_org_news import get_python_news
from web_app.model import db, News
from web_app.forms import LoginForm

def create_app():

    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('config.py')
    db.init_app(app)

    @app.route('/')
    def index():
        page_title = 'новости python'
        weather = weather_by_city(app.config['WEATHER_DEFAULT_CITY'])
        news_list = News.query.order_by(News.published.desc()).all()
        return render_template("index.html", page_title = page_title, weather=weather, news_list = news_list)

    @app.route('/login')
    def login():
        title = "Авторизация"
        login_form = LoginForm()
        return render_template("login.html",page_title=title, form=login_form)

    return app