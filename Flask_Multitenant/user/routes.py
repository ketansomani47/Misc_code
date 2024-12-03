from . import user_bp
from flask import make_response, jsonify, request
from models import User
from marshmallow import Schema, fields
from setup import db
from setting_db import get_tenant_session
from werkzeug.exceptions import abort
from datetime import datetime
from throttling import limiter
from flask_sqlalchemy import Pagination, BaseQuery

class UserSchema(Schema):
    Name = fields.String()
    Email = fields.String()
    Age = fields.Integer()
    ID = fields.Integer()
    CreatedAt = fields.DateTime()
    UpdatedAt = fields.DateTime()
    # rewards = fields.Method("split_data")
    #
    # def split_data(self, obj):
    #     if obj.rewards:
    #         return obj.rewards.split(",")
    #     return []

single_user = UserSchema()
multi_user = UserSchema(many=True)

from setting_db import tenant_required

@user_bp.route("/<string:tenant_name>/get", methods=["GET"])
@tenant_required
@limiter.limit("3/minute")
def user_data(tenant_session):
    # users = tenant_session.query(User).all()
    # return jsonify({tenant_name: [i.username for i in users]})
    page = 1
    per_page = 1
    user = tenant_session.query(User).paginate(page, per_page, error_out=True)
    # user = user.paginate(page, per_page, error_out=True)
    # pagination = Pagination(user, page, per_page, len(user))
    # data1 = multi_user.dump(pagination)
    # user = User.query.paginate(page, per_page, error_out=True)
    print(user)
    data1 = multi_user.dump(user)
    if len(data1) > 0:
        return make_response(jsonify({"message": "User List", "Data": data1}), 200)
    return make_response(jsonify({"message": "No User List Found"}), 204)

@user_bp.route("/<string:tenant_name>/post", methods=["POST"])
@tenant_required
@limiter.exempt()
def add_user(tenant_session):
    if request.get_json():
        data = request.get_json()
    # elif request.form:
    #     data = request.form
    # elif request.args:
    #     data = request.args
    else:
        return make_response(jsonify({"message": "Data required"}), 400)
    # tenant_session = get_tenant_session(tenant_name)
    # if not tenant_session:
    #     return make_response(jsonify({"message": "Invalid Tenant Name"}), 400)
    invalidate_user = single_user.validate(data)
    if invalidate_user:
        # print(invalidate_user)
        return make_response(jsonify({"message": invalidate_user}), 400)
    user = User()
    user.Name = data["Name"]
    user.Email = data["Email"]
    user.Age = data["Age"]
    user.CreatedAt = datetime.now()
    tenant_session.add(user)
    tenant_session.commit()
    # db.session.add(user)
    # db.session.commit()
    return make_response(jsonify({"message": "User Added Successfully"}), 201)


@user_bp.route("<string:tenant_name>/update/<int:id>", methods=["PUT"])
@tenant_required
def update_user(tenant_session, id):
    # print(request.get_json())
    # import pdb; pdb.set_trace()
    if request.get_json():
        data = request.get_json()
    # elif request.form:
    #     data = request.form
    # elif request.args:
    #     data = request.args
    else:
        return make_response(jsonify({"message": "Data required"}), 400)
    # tenant_session = get_tenant_session(tenant_name)
    # if not tenant_session:
    #     return make_response(jsonify({"message": "Invalid Tenant Name"}), 400)

    error = single_user.validate(data)
    if error:
        return make_response(jsonify({"message": error}), 400)
    # user = User.query.filter(User.ID == id).first()
    user = tenant_session.query(User).filter(User.ID == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    user.Email = data["Email"]
    user.Name = data["Name"]
    user.Age = data["Age"]
    user.UpdatedAt = datetime.now()
    tenant_session.commit()
    # db.session.commit()
    return make_response(jsonify({"message": "User Updated Successfully"}), 200)


@user_bp.route("<string:tenant_name>/delete/<int:id>", methods=["DELETE"])
@tenant_required
def delete_user(tenant_session, id):
    # tenant_session = get_tenant_session(tenant_name)
    # if not tenant_session:
    #     return make_response(jsonify({"message": "Invalid Tenant Name"}), 400)
    # user = User.query.filter(User.ID == id).first()
    user = tenant_session.query(User).filter(User.ID == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    tenant_session.delete(user)
    tenant_session.commit()
    # db.session.delete(user)
    # db.session.commit()
    return make_response(jsonify({"message": "User Deleted Successfully"}), 200)
