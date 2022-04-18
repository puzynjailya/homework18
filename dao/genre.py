from dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def read_all(self):
        return self.session.query(Genre).all()

    def read_one(self, gid):
        return self.session.query(Genre).get(gid)
