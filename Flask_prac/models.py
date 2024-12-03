import datetime
from setup import db

class User(db.Model):
    __tablename__ = "User"
    ID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(100))
    Age = db.Column(db.Integer())
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.now())
    UpdatedAt = db.Column(db.DateTime, default=datetime.datetime.now())

