from flask import Blueprint, request, jsonify
from app.controllers.auth_controller import signup

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def register():
    user = signup(request.json)
    return jsonify({"id": user.id, "username": user.username}), 201
