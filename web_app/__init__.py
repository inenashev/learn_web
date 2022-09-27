from flask import Flask
from flask_login import LoginManager
from web_app.db import db
from web_app.user.models import User
from web_app.user.views import blueprint as user_blueprint
from web_app.admin.views import blueprint as admin_blueprint
from web_app.news.views import blueprint as news_blueprint
def create_app():
    app = Flask(__name__, template_folder='../templates')
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
