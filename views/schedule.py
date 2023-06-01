from flask import request
from flask_restx import Namespace, Resource
from implemented import schedule_service, schedule_schema, schedules_schema

schedule_ns = Namespace("schedule")


@schedule_ns.route("/")
class SchedulesView(Resource):
    """
    Класс ScheduleView является подклассом класса Resource.
    Он предоставляет два метода для обработки запросов HTTP:
    get() и post().

    Метод get() используется для получения всех лекций из базы данных.
    Он возвращает данные в формате JSON.

    Метод post() используется для создания новой лекции.
    Он получает данные из запроса JSON и передает их в метод create() сервиса ScheduleService.
    Затем он возвращает созданную лекцию в формате JSON.
    """

    def get(self):
        lessons = schedule_service.get_all()
        return schedules_schema.dump(lessons), 200

    def post(self):
        data = request.json
        new_lesson = schedule_service.create(data)

        return schedule_schema.dump(new_lesson), 201


@schedule_ns.route("/<int:lid>")
class ScheduleView(Resource):
    """
    Класс ScheduleView является подклассом класса Resource.
    Он предоставляет четыре метода для обработки запросов HTTP:
    get(), put(), patch() и delete().

    Метод get() - используется для получения лекции с заданным идентификатором (lid).
    Он возвращает данные в формате JSON.

    Метод put() - используется для обновления лекции с заданным идентификатором (lid).
    Он возвращает данные в формате JSON.

    Метод patch() - используется для частичного обновления лекции с заданным идентификатором (lid).
    Он возвращает данные в формате JSON.

    Метод delete() - используется для удаления лекции с заданным идентификатором (lid).
    Он возвращает сообщение об успешном удалении лекции
    """

    def get(self, lid):
        lesson = schedule_service.get_one(lid)
        return schedule_schema.dump(lesson), 200

    def put(self, lid):
        data = request.json
        schedule_service.update(data, lid)

        lesson = schedule_service.get_one(lid)
        return schedule_schema.dump(lesson), 202

    def patch(self, lid):
        data = request.json
        schedule_service.update_partial(data, lid)

        lesson = schedule_service.get_one(lid)
        return schedule_schema.dump(lesson), 202

    def delete(self, lid):
        schedule_service.delete(lid)
        response = {"message": "lesson has deleted successfully"}

        return response, 200
