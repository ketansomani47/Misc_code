import os
from urllib.parse import quote_plus

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    API_KEY = os.environ.get("API_KEY") or "1381198b9480be4f347b385275a491f2"
    # API_KEY = os.environ.get("API_KEY") or "ketansomani"
    # Database
    SQLALCHEMY_DATABASE_URI = (
     os.environ.get("DATABASE_URL") or "mysql+pymysql://root:%s@localhost/flask" % quote_plus("Password@123")
    # +pymysql
     )
    # SQLALCHEMY_DATABASE_URI = (
    #     os.environ.get("DATABASE_URL") or "mysql://AdminZero:Orangeboy@aml-staging.cnse37g588ns.us-east-2.rds.amazonaws.com/amlstaging"
    #  )
    # Vishal local connection
    # SQLALCHEMY_DATABASE_URI = (
    #       os.environ.get("DATABASE_URL") or "mysql://root:Vishal@16@localhost/database"
    #  )
    SQLALCHEMY_BINDS = {
            'db1': "mysql+pymysql://root:%s@localhost/test1" % quote_plus("Password@123"),
            'db2': "mysql+pymysql://root:%s@localhost/test2" % quote_plus("Password@123")
    }
    # ----------------------------------------
    #
    # TEMP_PARAM = "mysql+mysqldb://root:Vishal@16@localhost/amlstaging"
    # TEMP_PARAM = 'mysql+pymysql://AdminZero:Orangeboy@aml-staging.cnse37g588ns.us-east-2.rds.amazonaws.com/amlstaging'

    # -------------------------
    ### NEW RDS
    # TEMP_PARAM = 'mysql+pymysql://AdminZero:Orangeboy@aml-penalties-db.caehnlyagu9k.us-west-1.rds.amazonaws.com/aml_staging_db'

    SQLALCHEMY_ECHO = os.environ.get("SQLALCHEMY_ECHO") or False
    SQLALCHEMY_TRACK_MODIFICATIONS = (
            os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS") or False
    )

    # S3
    # S3_BUCKET = "aml-zone-profile-pictures"
    # S3_LOCATION = "http://{}.s3.amazonaws.com/".format(S3_BUCKET)
    #
    # # Mail - Mailtrap.io
    # MAIL_SERVER = os.environ.get("MAIL_SERVER") or "smtp.gmail.com"
    # MAIL_PORT = os.environ.get("MAIL_PORT") or "465"
    # MAIL_USERNAME = os.environ.get("MAIL_USERNAME") or "zigram.amlzone@gmail.com"
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD") or "123@zigram"
    # MAIL_USE_TLS = os.environ.get("MAIL_USE_TLS") or False
    # MAIL_USE_SSL = os.environ.get("MAIL_USE_SSL") or True