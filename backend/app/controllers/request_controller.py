from app.services.assignment_service import auto_assign_team
from app.models.maintenance_request import MaintenanceRequest
from app.extensions import db

def create_request(data):
    team_id = auto_assign_team(data["equipment_id"])

    req = MaintenanceRequest(
        subject=data["subject"],
        request_type=data["type"],
        equipment_id=data["equipment_id"],
        team_id=team_id
    )

    db.session.add(req)
    db.session.commit()
    return req
