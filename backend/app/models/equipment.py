from app.extensions import db

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100))
    purchase_date = db.Column(db.Date)
    equipment_type = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Active")

    team_id = db.Column(db.Integer, db.ForeignKey("maintenance_team.id"))
    assigned_to = db.Column(db.Integer, db.ForeignKey("employee.id"), nullable = True)
