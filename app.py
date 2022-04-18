from flask import Flask
from flask_restx import Api
from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns
from create_data import upload_data


# Функция создания основного объекта app
def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    register_extensions(app)
    return app


# Функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(app):
    db.init_app(app)
    api = Api(app)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(movie_ns)
    create_data(app, db)


# Функция загрузки данных
def create_data(app, db):
    with app.app_context():
        upload_data(db)


app = create_app(Config())
app.debug = True


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
