from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def read_all(self):
        return self.dao.read_all()

    def read_one(self, mid):
        return self.dao.read_one(mid)

    def read_year(self, year):
        return self.dao.read_year(year)

    def read_director(self, director_id):
        return self.dao.read_director(director_id)

    def read_genre(self, genre_id):
        return self.dao.read_genre(genre_id)

    def create(self, data):
        return self.dao.create(data)

    def update(self, mid, data):
        entity = self.dao.read_one(mid)

        entity.title = data['title']
        entity.description = data['description']
        entity.trailer = data['trailer']
        entity.year = data['year']
        entity.rating = data['rating']
        entity.genre_id = data['genre_id']
        entity.director_id = data['director_id']

        self.dao.update(entity)

    def update_partial(self, mid, data):
        entity = self.dao.read_one(mid)
        if 'title' in data.keys():
            entity.title = data['title']
        if 'description' in data.keys():
            entity.description = data['description']
        if 'trailer' in data.keys():
            entity.trailer = data['trailer']
        if 'year' in data.keys():
            entity.year = data['year']
        if 'rating' in data.keys():
            entity.rating = data['rating']
        if 'genre_id' in data.keys():
            entity.genre_id = data['genre_id']
        if 'director_id' in data.keys():
            entity.director_id = data['director_id']

        self.dao.update(entity)

    def delete(self, mid):
        self.dao.delete(mid)

