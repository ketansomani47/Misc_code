from flask import jsonify, Flask, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    return "code is running"

@app.route("/free", methods=["GET"])
def hello1():
    return "free code is running"


@app.route("/user", methods=["GET"])
def user():
    return make_response(jsonify({"message": "Lambda is working"}), 200)


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all(bind="__all__")
    app.run(debug=True)


