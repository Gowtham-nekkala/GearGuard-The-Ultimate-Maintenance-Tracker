from app.extensions import db
from datetime import datetime

class MaintenanceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(200), nullable=False)
    request_type = db.Column(db.String(20))
    status = db.Column(db.String(20), default="New")
    priority = db.Column(db.String(20))

    scheduled_date = db.Column(db.Date)
    duration = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    equipment_id = db.Column(db.Integer, db.ForeignKey("equipment.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("maintenance_team.id"))
    assigned_to = db.Column(db.Integer, db.ForeignKey("employee.id"))

