from setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text())
    trailer = db.Column(db.String(150))
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Задаем связи
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genres = db.relationship('Genre', lazy=True)

    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    directors = db.relationship('Director', lazy=True)


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()

    genre_id = fields.Int()
    genre = fields.Nested('Genre')

    director_id = fields.Int()
    director = fields.Nested('Director')