import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    # TODO: Disable This While deploying
    app.config.from_object(config_class)
    db.init_app(app)
    migrate.init_app(app, db)

    return app

import models
