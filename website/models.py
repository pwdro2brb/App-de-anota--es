from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    data = db.column(db.DateTime(timezone=True), default=func.now())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.string(150), unique = True)
    password = db.Column(db.string(150))
    Primeiro_nome = db.Column(db.string(150))
