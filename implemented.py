from dao.notes_dao import NotesDAO
from services.notes_service import NotesServices
from dao.models.notes import NotesSchema
from setup_db import db

note_dao = NotesDAO(db.session)
note_service = NotesServices(dao=note_dao)

note_schema = NotesSchema()
notes_schema = NotesSchema(many=True)
