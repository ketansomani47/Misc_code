from flask_cors import CORS
from setup import db, create_app
from user import user_bp as bp
from flask import jsonify
import threading
import asyncio

application = app = create_app()
CORS(app)
app.register_blueprint(bp, url_prefix="/user")



@app.route("/", methods=["GET"])
def hello():
    return "code is running"

# @app.route("/test", methods=["GET"])
# def index():
#     print(f"Inside flask function: {threading.current_thread().name}")
#     asyncio.set_event_loop(asyncio.new_event_loop())
#     loop = asyncio.get_event_loop()
#     result = loop.run_until_complete(hello())
#     return jsonify({"result": result})
#
#
# async def hello():
#     await asyncio.sleep(15)
#     return 1


# app.test_client().get('')

if __name__ == '__main__':
    with app.app_context():
        db.create_all(bind="__all__")
    app.run(debug=True)
