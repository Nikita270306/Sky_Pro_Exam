from dao.notes_dao import NotesDAO


class NotesServices:

    def __init__(self, dao: NotesDAO):
        self.dao = dao

    def get_one(self, nid):
        return self.dao.get_one(nid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, nid):
        note = self.dao.get_one(nid)

        note.text = data.get("text")
        self.dao.update(note)

    def update_partial(self, data, nid):
        note = self.dao.get_one(nid)
        if "text" in data:
            note.text = data.get("text")

        self.dao.update(note)

    def delete(self, nid):
        return self.dao.delete(nid)
