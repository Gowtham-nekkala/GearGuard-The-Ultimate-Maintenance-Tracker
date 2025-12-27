from flask import Blueprint, request, jsonify
from app.controllers import (
    create_request,
    update_request_status
)

maintenance_bp = Blueprint("maintenance", __name__)

@maintenance_bp.route("/requests", methods=["POST"])
def create():
    data = request.json
    req = create_request(data)
    return jsonify({"id": req.id}), 201


@maintenance_bp.route("/requests/<int:request_id>/status", methods=["PUT"])
def update_status(request_id):
    data = request.json
    update_request_status(request_id, data["status"])
    return jsonify({"message": "Status updated"}), 200
