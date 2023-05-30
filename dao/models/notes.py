from setup_db import db
from marshmallow import Schema, fields
from sqlalchemy.sql import func


class Notes(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    data_added = db.Column(db.DateTime, default=func.now())


class NotesSchema(Schema):
    id = fields.Int(dump_only=True)
    text = fields.Str()
    data_added = fields.DateTime(dump_only=True)
