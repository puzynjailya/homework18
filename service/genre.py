from dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def read_all(self):
        return self.dao.read_all()

    def read_one(self, gid):
        return self.dao.read_one(gid)
