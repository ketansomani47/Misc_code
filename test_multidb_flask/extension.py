from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)
db = SQLAlchemy(app)
mg = Migrate(app, db)