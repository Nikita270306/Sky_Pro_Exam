from dao.schedule_dao import ScheduleDAO
from services.schedule_service import ScheduleServices
from dao.models.schedule import ScheduleSchema
from setup_db import db

schedule_dao = ScheduleDAO(db.session)
schedule_service = ScheduleServices(dao=schedule_dao)

schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)
