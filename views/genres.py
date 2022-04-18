from flask_restx import Resource, Namespace
from implemented import genre_service
from dao.model.genre import GenreSchema

genre_ns = Namespace('genres')


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        genres = genre_service.read_all()
        return genres_schema.dump(genres), 200


@genre_ns.route('/<int:did>')
class GenreView(Resource):
    def get(self, did):
        genre = genre_service.read_one(did)
        return genre_schema.dump(genre), 200
