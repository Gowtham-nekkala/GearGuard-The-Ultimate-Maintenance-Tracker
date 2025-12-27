from flask import Blueprint, request, jsonify
from app.controllers.request_controller import create_request

maintenance_bp = Blueprint("maintenance", __name__)

@maintenance_bp.route("/requests", methods=["POST"])
def create():
    req = create_request(request.json)
    return jsonify({"id": req.id})
