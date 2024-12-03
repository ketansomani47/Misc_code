from flask_sqlalchemy import SQLAlchemy
# db = SQLAlchemy()
from extension import db

class User(db.Model):
    __tablename__ = "user"
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    rewards = db.Column(db.Text)

class User1(db.Model):
    __bind_key__ = "db1"
    __tablename__ = "user"
    #__table_args__ = {'extend_existing': True}
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    rewards = db.Column(db.Text)

class User2(db.Model):
    __bind_key__ = "db2"
    __tablename__ = "user"
    #__table_args__ = {'extend_existing': True}
    s_no = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    rewards = db.Column(db.Text)
