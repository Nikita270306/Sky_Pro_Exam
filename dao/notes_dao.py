from dao.models.notes import Notes


class NotesDAO:

    def __init__(self, session):
        self.session = session

    def get_one(self, nid):
        return self.session.query(Notes).get(nid)

    def get_all(self):
        return self.session.query(Notes).all()

    def create(self, data):
        note = Notes(**data)

        self.session.add(note)
        self.session.commit()

        return note

    def update(self, note):
        self.session.add(note)
        self.session.commit()

    def delete(self, nid):
        note = self.get_one(nid)
        self.session.delete(note)
        self.session.commit()
