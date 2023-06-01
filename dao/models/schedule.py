from setup_db import db
from marshmallow import Schema, fields


class Schedule(db.Model):
    __tablename__ = 'schedule'

    id = db.Column(db.Integer, primary_key=True)
    lesson = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    teacher = db.Column(db.String(100), nullable=False)
    cabinet = db.Column(db.Integer, nullable=False)


class ScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    lesson = fields.Str()
    date = fields.Str()
    teacher = fields.Str()
    cabinet = fields.Int()
