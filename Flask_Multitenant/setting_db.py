from setup import db
from application import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# @simple_cache
# def get_known_tenants():
#     tenants = Tenant.query.all()
#     return [i.name for i in tenants]


def prepare_bind(tenant_name):
    # print(app.config['SQLALCHEMY_BINDS'])
    if tenant_name not in app.config['SQLALCHEMY_BINDS']:
        return None
        # raise Exception("Not a valid Tenant")
        # app.config['SQLALCHEMY_BINDS'][tenant_name] = MYSQL_URI.format(tenant_name)
    return app.config['SQLALCHEMY_BINDS'][tenant_name]


def get_tenant_session(tenant_name):
    # if tenant_name not in get_known_tenants():
    #     return None
    # try:
        conn_str = prepare_bind(tenant_name)
        # engine = db.get_engine(app, bind=tenant_name)
        if conn_str:
            engine = create_engine(conn_str)
            session_maker = sessionmaker(bind=engine)
            # session_maker.configure()
            session = session_maker()
            return session
        return None
    # except Exception as e:
    #     print(e)


from functools import wraps
from flask import make_response, jsonify
def tenant_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        tenant_session = get_tenant_session(kwargs["tenant_name"])
        if not tenant_session:
            return make_response(jsonify({"message": "Invalid Tenant Name"}), 400)
        kwargs.pop("tenant_name")
        return f(tenant_session, *args, **kwargs)
    return decorator
