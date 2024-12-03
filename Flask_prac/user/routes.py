from . import user_bp
from flask import make_response, jsonify, request
from models import User
from marshmallow import Schema, fields
from setup import db

class UserSchema(Schema):
    Name = fields.String()
    Email = fields.String()
    Age = fields.Integer()
    ID = fields.Integer()
    # rewards = fields.Method("split_data")
    #
    # def split_data(self, obj):
    #     if obj.rewards:
    #         return obj.rewards.split(",")
    #     return []

single_user = UserSchema()
multi_user = UserSchema(many=True)

@user_bp.route("/get", methods=["GET"])
def user_data():
    user = User.query.all()
    data1 = multi_user.dump(user)
    if len(data1) > 0:
        return make_response(jsonify({"message": "User List", "Data": data1}), 200)
    return make_response(jsonify({"message": "No User List Found"}), 204)

@user_bp.route("/post", methods=["POST"])
def add_user():
    if request.get_json():
        data = request.get_json()
    # elif request.form:
    #     data = request.form
    # elif request.args:
    #     data = request.args
    else:
        return make_response(jsonify({"message": "Data required"}), 400)
    invalidate_user = single_user.validate(data)
    if invalidate_user:
        # print(invalidate_user)
        return make_response(jsonify({"message": invalidate_user}), 400)
    user = User()
    user.Name = data["Name"]
    user.Email = data["Email"]
    user.Age = data["Age"]
    db.session.add(user)
    db.session.commit()
    return make_response(jsonify({"message": "User Added Successfully"}), 201)


@user_bp.route("/update/<int:id>", methods=["PUT"])
def update_user(id):
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
    error = single_user.validate(data)
    if error:
        return make_response(jsonify({"message": error}), 400)
    user = User.query.filter(User.ID == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    user.Email = data["Email"]
    user.Name = data["Name"]
    user.Age = data["Age"]
    db.session.commit()
    return make_response(jsonify({"message": "User Updated Successfully"}), 200)


@user_bp.route("/delete/<int:id>", methods=["DELETE"])
def delete_user(id):
    user = User.query.filter(User.ID == id).first()
    if not user:
        return make_response(jsonify({"message": "Invalid User"}), 400)
    db.session.delete(user)
    db.session.commit()
    return make_response(jsonify({"message": "User Deleted Successfully"}), 200)
