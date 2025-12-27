from app.extensions import db
from app.models.maintenance_request import MaintenanceRequest
from app.models.equipment import Equipment
from app.utils.enums import RequestStatus

def assign_technician(request_id, employee_id):
    req = MaintenanceRequest.query.get_or_404(request_id)
    req.assigned_to = employee_id
    req.status = RequestStatus.IN_PROGRESS
    db.session.commit()
    return req


def mark_repaired(request_id, duration):
    req = MaintenanceRequest.query.get_or_404(request_id)
    req.duration = duration
    req.status = RequestStatus.REPAIRED
    db.session.commit()
    return req


def mark_scrap(request_id):
    req = MaintenanceRequest.query.get_or_404(request_id)
    req.status = RequestStatus.SCRAP

    equipment = Equipment.query.get(req.equipment_id)
    if equipment:
        equipment.status = "Scrapped"

    db.session.commit()
    return req
