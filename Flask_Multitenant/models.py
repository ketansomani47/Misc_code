import datetime
from setup import db

class User(db.Model):
    __tablename__ = "User"
    # __bind_key__ = ["user1", "user2"]
    ID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(100))
    Age = db.Column(db.Integer())
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.now())
    UpdatedAt = db.Column(db.DateTime, default=datetime.datetime.now())

class User1(db.Model):
    __tablename__ = "User1"
    # __table_args__ = {'extend_existing': True}
    # __bind_key__ = "user2"
    ID = db.Column(db.Integer(), primary_key=True)
    Name = db.Column(db.String(255))
    Email = db.Column(db.String(100))
    Age = db.Column(db.Integer())
    CreatedAt = db.Column(db.DateTime, default=datetime.datetime.now())
    UpdatedAt = db.Column(db.DateTime, default=datetime.datetime.now())

