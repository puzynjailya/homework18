from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from flask import json
import os

FOLDER_PATH = 'static/data'
FILE_PATH = os.path.join(FOLDER_PATH, 'movies_data.json')


def upload_data(db):
    """
    Функция загрузки данных в БД
    :return: ничего. Просто создает данные в БД
    """
    db.drop_all()
    db.create_all()


    # Открываем файл json и загружаем данные
    with open(FILE_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Подгружаем данные фильмов
    for movie in data["movies"]:
        m = Movie(
            id=movie["pk"],
            title=movie["title"],
            description=movie["description"],
            trailer=movie["trailer"],
            year=movie["year"],
            rating=movie["rating"],
            genre_id=movie["genre_id"],
            director_id=movie["director_id"],
        )
        with db.session.begin():
            db.session.add(m)

    # Подгружаем данные режиссеров
    for director in data["directors"]:
        d = Director(
            id=director["pk"],
            name=director["name"],
        )
        with db.session.begin():
            db.session.add(d)

    # Подгружаем данные фильмов
    for genre in data["genres"]:
        d = Genre(
            id=genre["pk"],
            name=genre["name"],
        )
        with db.session.begin():
            db.session.add(d)
