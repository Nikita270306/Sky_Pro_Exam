from dao.schedule_dao import ScheduleDAO


class ScheduleServices:
    """
    Класс ScheduleServices представляет собой сервис, который позволяет взаимодействовать с лекциями через методы.

    __init__(self, dao: ScheduleDAO):
        Конструктор класса. Принимает объект ScheduleDAO в качестве аргумента.

    get_one(self, lid):
        Возвращает одну лекцию по ее идентификатору.

    get_all(self):
        Возвращает список всех лекций.

    create(self, data):
        Создает новую лекцию с переданными данными.

    update(self, data, lid):
        Обновляет лекцию по ее идентификатору с переданными данными.

    update_partial(self, data, lid):
        Обновляет часть лекции по ее идентификатору с переданными данными.

    delete(self, lid):
        Удаляет лекцию по ее идентификатору.
    """
    def __init__(self, dao: ScheduleDAO):
        self.dao = dao

    def get_one(self, lid):
        return self.dao.get_one(lid)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        return self.dao.create(data)

    def update(self, data, lid):
        lecture = self.dao.get_one(lid)

        lecture.lesson = data.get("lesson")
        lecture.date = data.get("date")
        lecture.teacher = data.get("teacher")
        lecture.cabinet = data.get("cabinet")

        self.dao.update(lecture)

    def update_partial(self, data, lid):
        lecture = self.dao.get_one(lid)
        if "lesson" in data:
            lecture.lesson = data.get("lesson")
        if "date" in data:
            lecture.date = data.get("date")
        if "teacher" in data:
            lecture.teacher = data.get("teacher")
        if "cabinet" in data:
            lecture.cabinet = data.get("cabinet")

        self.dao.update(lecture)

    def delete(self, lid):
        return self.dao.delete(lid)
