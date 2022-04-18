from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    # Считываем все фильмы
    def read_all(self):
        return self.session.query(Movie).all()

    # Считываем один фильм по id
    def read_one(self, mid):
        return self.session.query(Movie).filter(Movie.id == mid).one()

    def read_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year).all()

    def read_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id).all()

    def read_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id).all()

    # Добавляем фильм в БД
    def create(self, data):
        entity = Movie(**data)
        self.session.add(entity)
        self.session.commit()

        return entity

    # Обновляем данные
    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

    # Удаляем данные по id
    def delete(self, mid):
        movie = self.read_one(mid)
        self.session.delete(movie)
        self.session.commit()
