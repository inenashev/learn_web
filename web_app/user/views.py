from web_app.db import db
from web_app.user.models import User
from web_app.user.forms import LoginForm, RegistrationForm
from flask_login import login_user,logout_user,current_user, login_required
from flask import Blueprint, render_template, flash, redirect, url_for

blueprint = Blueprint('user', __name__, url_prefix='/users')


@blueprint.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Авторизация"
    login_form = LoginForm()
    return render_template("user/login.html",page_title=title, form=login_form)


@blueprint.route("/process-login", methods=['POST'])
def process_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash("вы успешно вошли")
            return redirect(url_for('news.index'))
    flash("Неправильный логин или пароль")
    return redirect(url_for('user.login'))

@blueprint.route("/logout")
def logout():
    logout_user()
    flash("Вы успешно разлогинились")
    return redirect(url_for("news.index"))

@blueprint.route("/register")
def register():
    if current_user.is_authenticated:
        return redirect(url_for('news.index'))
    title = "Регистрация"
    reg_form = RegistrationForm()
    return render_template("user/registration.html", page_title=title, form=reg_form)


@blueprint.route("/process-reg", methods=['POST'])
def process_reg():
    form = RegistrationForm()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        role='user')
        new_user.set_password(form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash("вы успешно зарегистрированы")
        return redirect(url_for('user.login'))
    #flash('Пожалуйста, исправьте ошибки в форме')
    #return redirect(url_for('user.register'))
    else:
        for field, errors in form.errors.items():
            for error in errors:
                flash('Ошибка в поле {}: {}'.format(
                    getattr(form,field).label.text,error
                ))
        return redirect(url_for('user.register'))