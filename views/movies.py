from flask_restx import Resource, Namespace
from flask import request, abort, Response
from dao.model.movie import MovieSchema
from implemented import movie_service

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # Считываем аргументы, если они есть
        year = request.args.get('year')
        genre_id = request.args.get('genre_id')
        director_id = request.args.get('director_id')

        # Проверяем аргументы и при наличии возвращаем обработку сервисов
        if year:
            movies = movie_service.read_year(year)
            return movies_schema.dump(movies), 200

        if genre_id:
            movies = movie_service.read_genre(genre_id)
            return movies_schema.dump(movies), 200

        if director_id:
            movies = movie_service.read_director(director_id)
            return movies_schema.dump(movies), 200

        movies = movie_service.read_all()
        return movies_schema.dump(movies), 200

    def post(self):

        data = request.json
        movie = movie_service.create(data)
        response = Response('', 201, mimetype='application/json')
        response.headers['Location'] = str(movie.id)
        return response


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.read_one(mid)
        if not movie:
            return abort (404)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        data = request.json
        movie_service.update(mid, data)
        return '', 204

    def patch(self, mid):
        data = request.json
        movie_service.update_partial(mid, data)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204
