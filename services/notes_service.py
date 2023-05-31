from dao.notes_dao import NotesDAO


class NotesServices:
    """
    Класс NotesServices представляет собой сервис, который позволяет взаимодействовать с заметками через методы.

    __init__(self, dao: NotesDAO):
        Конструктор класса. Принимает объект NotesDAO в качестве аргумента.

    get_one(self, nid):
        Возвращает одну заметку по ее идентификатору.

    get_all(self):
        Возвращает список всех заметок.

    create(self, data):
        Создает новую заметку с переданными данными.

    update(self, data, nid):
        Обновляет заметку по ее идентификатору с переданными данными.

    update_partial(self, data, nid):
        Обновляет часть заметки по ее идентификатору с переданными данными.

    delete(self, nid):
        Удаляет заметку по ее идентификатору.
    """
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
