from flask import Flask, request, jsonify, make_response, current_app
from flask_sqlalchemy import SQLAlchemy
from User import user_bp
from flask_migrate import Migrate
from config import Config
import models
from extension import app
from urllib.parse import quote_plus
# app = Flask(__name__)
app.config.from_object(Config)
# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/flask" % quote_plus("Password@123")

app.register_blueprint(user_bp)

@app.route("/test", methods=["GET"])
def hello():
    return make_response(jsonify({"message": "Hello User!!"}), 200)

if __name__ == "__main__":
    # db.create_all()
    # print(app.config)
    app.run(debug=True)
