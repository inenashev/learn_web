from flask import Flask, render_template, flash, redirect, url_for
from flask_login import LoginManager, login_user
from web_app.weather import weather_by_city
from web_app.python_org_news import get_python_news
from web_app.model import db, News, User
from web_app.forms import LoginForm


def create_app():

    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

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


    @app.route("/process-login", methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter(User.username == form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash("вы успешно вошли")
                return redirect(url_for('index'))
        flash("Неправильный логин или пароль")
        return redirect(url_for('login'))


    return app