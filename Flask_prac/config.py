import os
from urllib.parse import quote_plus

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Universal
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    API_KEY = os.environ.get("API_KEY") or "1381198b9480be4f347b385275a491f2"
    #Database
    SQLALCHEMY_DATABASE_URI = (
     # os.environ.get("DATABASE_URL") or "mysql://root:Password@123@localhost/flask_prac"
     os.environ.get("DATABASE_URL") or "mysql+pymysql://root:%s@localhost/flask_prac" % quote_plus("Password@123")
     )
    DEBUG_TB_PROFILER_ENABLED = True
    # TEMP_PARAM = 'mysql://root:Password@123@localhost:3306/flask_prac'

    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO") or False
    SQLALCHEMY_TRACK_MODIFICATIONS = (
        os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False
    )

