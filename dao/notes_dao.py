from dao.models.notes import Notes


class NotesDAO:
    """
    NotesDAO - класс для работы с данными из БД

    __init__(self, session) - конструктор класса
        session - сессия для работы с БД

    get_one(self, nid) - получение заметки из БД по id
        nid - id заметки

    get_all(self) - получение всех заметок из БД

    create(self, data) - создание заметки в БД
        data - данные для создания заметки

    update(self, note) - обновление данных заметки в БД
        note - объект заметки

    delete(self, nid) - удаление заметки из БД
        nid - id заметки
    """
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
