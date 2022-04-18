from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def read_all(self):
        return self.dao.read_all()

    def read_one(self, did):
        return self.dao.read_one(did)
