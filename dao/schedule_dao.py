from dao.models.schedule import Schedule


class ScheduleDAO:
    """
    ScheduleDAO - класс для работы с данными из БД

    __init__(self, session) - конструктор класса
        session - сессия для работы с БД

    get_one(self, lid) - получение лекции из БД по id
        lid - id лекции

    get_all(self) - получение всех лекций из БД

    create(self, data) - создание лекции в БД
        data - данные для создания новой лекции

    update(self, lecture) - обновление данных лекции в БД
        lecture - объект лекции

    delete(self, lid) - удаление лекции из БД
        lid - id лекции
    """
    def __init__(self, session):
        self.session = session

    def get_one(self, lid):
        return self.session.query(Schedule).get(lid)

    def get_all(self):
        return self.session.query(Schedule).all()

    def create(self, data):
        lecture = Schedule(**data)

        self.session.add(lecture)
        self.session.commit()

        return lecture

    def update(self, lecture):
        self.session.add(lecture)
        self.session.commit()

    def delete(self, lid):
        lecture = self.get_one(lid)
        self.session.delete(lecture)
        self.session.commit()
