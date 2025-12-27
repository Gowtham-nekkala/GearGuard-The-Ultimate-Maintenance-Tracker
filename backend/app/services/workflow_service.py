from datetime import datetime
from app.extensions import db
from app.models.maintenance_request import MaintenanceRequest
from app.utils.enums import RequestStatus

class WorkflowService:

    # Allowed state transitions
    VALID_TRANSITIONS = {
        RequestStatus.NEW: [RequestStatus.IN_PROGRESS, RequestStatus.SCRAP],
        RequestStatus.IN_PROGRESS: [RequestStatus.REPAIRED, RequestStatus.SCRAP],
        RequestStatus.REPAIRED: [],
        RequestStatus.SCRAP: []
    }

    @staticmethod
    def process_state_change(request_id, new_status, duration=None, user_id=None):
        req = MaintenanceRequest.query.get(request_id)
        if not req:
            raise ValueError("Maintenance request not found")

        old_status = req.status

        if old_status == new_status:
            return req  # no-op

        if new_status not in WorkflowService.VALID_TRANSITIONS.get(old_status, []):
            raise ValueError(f"Invalid transition from {old_status} to {new_status}")

        req.status = new_status

        # Technician picks up job
        if new_status == RequestStatus.IN_PROGRESS and user_id:
            if not req.assigned_to:
                req.assigned_to = user_id

        # Completion logic
        if new_status == RequestStatus.REPAIRED:
            req.completion_date = datetime.utcnow()
            if duration is not None:
                req.duration = float(duration)

        # Scrap logic
        if new_status == RequestStatus.SCRAP:
            req.completion_date = datetime.utcnow()
            if req.equipment:
                req.equipment.status = "Scrapped"

        db.session.commit()
        return req
