from dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def read_all(self):
        return self.session.query(Director).all()

    def read_one(self, did):
        return self.session.query(Director).get(did)

