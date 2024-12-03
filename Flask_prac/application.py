from flask_cors import CORS
from setup import db, create_app
from user import user_bp as bp

application = app = create_app()
CORS(app)
app.register_blueprint(bp, url_prefix="/user")


@app.route("/", methods=["GET"])
def hello():
    return "code is running"

app.test_client().get('')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
