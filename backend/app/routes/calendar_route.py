from flask import Blueprint, jsonify
from app.controllers.request_controller import get_calendar_events

calendar_bp = Blueprint("calendar", __name__)

@calendar_bp.route("/", methods=["GET"])
def calendar():
    events = get_calendar_events()
    return jsonify(events), 200
