from flask import Blueprint, jsonify
from app.controllers import get_kanban_board

kanban_bp = Blueprint("kanban", __name__)

@kanban_bp.route("/", methods=["GET"])
def kanban_board():
    board = get_kanban_board()
    return jsonify(board), 200
