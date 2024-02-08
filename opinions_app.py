# what_to_watch/opinions_app.py
from datetime import datetime

# Импортируется функция выбора случайного значения
from random import randrange

# Добавлена функция render_template
from flask import Flask, render_template
# Импортируется нужный класс для работы с ORM
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# Подключается БД SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
# В ORM передаётся в качестве параметра экземпляр приложения Flask
# Задаётся конкретное значение для конфигурационного ключа
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Opinion(db.Model):
    # ID — целое число, первичный ключ
    id = db.Column(db.Integer, primary_key=True)
    # Название фильма — строка длиной 128 символов, не может быть пустым
    title = db.Column(db.String(128), nullable=False)
    # Мнение о фильме — большая строка, не может быть пустым,
    # должно быть уникальным
    text = db.Column(db.Text, unique=True, nullable=False)
    # Ссылка на сторонний источник — строка длиной 256 символов
    source = db.Column(db.String(256))
    # Дата и время — текущее время,
    # по этому столбцу база данных будет проиндексирована
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)


@app.route('/')
def index_view():
    # Определяется количество мнений в базе данных
    quantity = Opinion.query.count()
    # Если мнений нет,
    if not quantity:
        # то возвращается сообщение
        return 'В базе данных мнений о фильмах нет.'
    # Иначе выбирается случайное число в диапазоне от 0 и до quantity
    offset_value = randrange(quantity)
    # И определяется случайный объект
    opinion = Opinion.query.offset(offset_value).first()
    # Вот здесь в шаблон передаётся весь объект opinion
    return render_template('opinion.html', opinion=opinion)


@app.route('/add')
def add_opinion_view():
    return render_template('add_opinion.html')


if __name__ == '__main__':
    app.run()
