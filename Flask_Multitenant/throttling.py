from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from application import app
from flask import request
# print(get_remote_address())

def my_func(*args, **kwargs):
    print(request.args)
    user_id = request.args["user_id"]
    return user_id

limiter = Limiter(app, key_func=my_func, default_limits=["2/hours", "1/second", "1/minute"])