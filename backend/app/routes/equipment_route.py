from flask import Blueprint, request, jsonify
from app.controllers import (
    create_equipment,
    get_all_equipment,
    get_equipment_by_id
)

equipment_bp = Blueprint("equipment", __name__)

@equipment_bp.route("/", methods=["POST"])
def create():
    data = request.json
    equipment = create_equipment(data)
    return jsonify({"id": equipment.id}), 201


@equipment_bp.route("/", methods=["GET"])
def get_all():
    equipments = get_all_equipment()
    return jsonify(equipments), 200


@equipment_bp.route("/<int:equipment_id>", methods=["GET"])
def get_by_id(equipment_id):
    equipment = get_equipment_by_id(equipment_id)
    return jsonify(equipment), 200
