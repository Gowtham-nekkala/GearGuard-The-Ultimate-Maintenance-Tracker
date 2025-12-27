from datetime import datetime
from app.extensions import db
from app.models import MaintenanceRequest
from app.services.assignment_service import auto_assign_team
from app.services.workflow_service import WorkflowService
from app.utils.enums import RequestStatus

def create_request(data):
    team_id = auto_assign_team(data["equipment_id"])

    req = MaintenanceRequest(
        subject=data["subject"],
        request_type=data["request_type"],
        equipment_id=data["equipment_id"],
        team_id=team_id,
        priority=data.get("priority"),
        scheduled_date=data.get("scheduled_date"),
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
        status=RequestStatus.NEW
    )

    db.session.add(req)
    db.session.commit()
    return req


def update_request_status(request_id, data):
    return WorkflowService.process_state_change(
        request_id=request_id,
        new_status=data["status"],
        duration=data.get("duration"),
        user_id=data.get("user_id")
    )


def get_kanban_board():
    requests = MaintenanceRequest.query.all()

    board = {
        RequestStatus.NEW: [],
        RequestStatus.IN_PROGRESS: [],
        RequestStatus.REPAIRED: [],
        RequestStatus.SCRAP: []
    }

    for r in requests:
        board[r.status].append({
            "id": r.id,
            "subject": r.subject,
            "equipment_id": r.equipment_id,
            "team_id": r.team_id,
            "assigned_to": r.assigned_to
        })

    return board


def get_calendar_events():
    preventive_requests = MaintenanceRequest.query.filter_by(
        request_type="Preventive"
    ).all()

    return [
        {
            "id": r.id,
            "title": r.subject,
            "start": r.scheduled_date.isoformat(),
            "status": r.status
        }
        for r in preventive_requests if r.scheduled_date
    ]
