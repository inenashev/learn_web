from getpass import getpass
import sys

from web_app import create_app
from web_app.db import db,User

app = create_app()

with app.app_context():
    username = input('Введите имя:')

    if User.query.filter(User.username == username).count():
        print("Такой уже есть")
        sys.exit(1)

    password1 = getpass('Введите пароль')
    password2 = getpass('Введите пароль')

    if not password1 == password2:
        print("пароли не одинаковые")
        sys.exit(1)

    new_user = User(username=username,role='admin')
    new_user.set_password(password1)

    db.session.add(new_user)
    db.session.commit()
    print(f"Создан пользватель с id {new_user.id}")