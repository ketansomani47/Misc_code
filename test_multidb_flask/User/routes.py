from . import user_bp
from flask import make_response, jsonify, request
from models import User
from marshmallow import Schema, fields
from extension import db
class UserSchema(Schema):
    name = fields.String(required=True)
    email = fields.Email(required=True)
    rewards = fields.Method("split_data")

    def split_data(self, obj):
        if obj.rewards:
            return obj.rewards.split(",")
        return []

single_user = UserSchema()
multi_user = UserSchema(many=True)

@user_bp.route("/get", methods=["GET"])
def user_data():
    user = User.query.all()
    # data1 = []
    data1 = multi_user.dump(user)
    # for i in user:
    #     data = {}
    #     print(i)
    #     data["Name"] = i.name
    #     data["Email"] = i.email
    #     data1.append(data)
    if len(data1) > 0:
        return make_response(jsonify({"message": "User List", "Data": data1}), 200)
    return make_response(jsonify({"message": "No User List Found"}), 204)

@user_bp.route("/post", methods=["POST"])
def add_user():
    # print(request.get_json())
    if request.get_json():
        data = request.get_json()
    elif request.form:
        data = request.form
    elif request.args:
        data = request.args
    else:
        return make_response(jsonify({"message": "Data required"}), 400)
    invalidate_user = single_user.validate(data)
    if invalidate_user:
        # print(invalidate_user)
        return make_response(jsonify({"message": invalidate_user}), 400)
    user = User()
    user.name = data["name"]
    user.email = data["email"]
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({"message": "User Added Successfully"}), 200)


@user_bp.route("/update/<int:id>", methods=["PUT"])
def update_user(id):
    # print(request.get_json())
    if request.get_json():
        data = request.get_json()
    elif request.form:
        data = request.form
    elif request.args:
        data = request.args
    else:
        return make_response(jsonify({"message": "Data required"}), 400)
    error = single_user.validate(data)
    if error:
        return make_response(jsonify({"message": error}), 400)
    user = User.query.filter(User.s_no == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    user.email = data["email"]
    user.name = data["name"]
    db.session.commit()
    return make_response(jsonify({"message": "User Updated Successfully"}), 200)


@user_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.filter(User.s_no == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({"message": "User Deleted Successfully"}), 200)
