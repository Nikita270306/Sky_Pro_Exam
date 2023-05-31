from flask import request
from flask_restx import Namespace, Resource
from implemented import note_service, note_schema, notes_schema

note_ns = Namespace("notes")


@note_ns.route("/")
class NotesView(Resource):
    """
    Класс NotesView является подклассом класса Resource.
    Он предоставляет два метода для обработки запросов HTTP:
    get() и post().

    Метод get() используется для получения всех заметок из базы данных.
    Он возвращает данные в формате JSON.

    Метод post() используется для создания новой заметки.
    Он получает данные из запроса JSON и передает их в метод create() сервиса NoteService.
    Затем он возвращает созданную заметку в формате JSON.
    """

    def get(self):
        notes = note_service.get_all()
        return notes_schema.dump(notes), 200

    def post(self):
        data = request.json
        new_note = note_service.create(data)

        return note_schema.dump(new_note), 201


@note_ns.route("/<int:nid>")
class NoteView(Resource):
    """
    Класс NoteView является подклассом класса Resource.
    Он предоставляет четыре метода для обработки запросов HTTP:
    get(), put(), patch() и delete().

    Метод get() - используется для получения заметки с заданным идентификатором (nid).
    Он возвращает данные в формате JSON.

    Метод put() - используется для обновления заметки с заданным идентификатором (nid).
    Он возвращает данные в формате JSON.

    Метод patch() - используется для частичного обновления заметки с заданным идентификатором (nid).
    Он возвращает данные в формате JSON.

    Метод delete() - используется для удаления заметки с заданным идентификатором (nid).
    ОН возвращает сообщение об успешном удалении заметки
    """

    def get(self, nid):
        note = note_service.get_one(nid)
        return note_schema.dump(note), 200

    def put(self, nid):
        data = request.json
        note_service.update(data, nid)

        note = note_service.get_one(nid)
        return note_schema.dump(note), 202

    def patch(self, nid):
        data = request.json
        note_service.update_partial(data, nid)

        note = note_service.get_one(nid)
        return note_schema.dump(note), 202

    def delete(self, nid):
        note_service.delete(nid)
        response = {"message": "Note has deleted successfully"}

        return response, 200
