from app.extensions import db

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    serial_number = db.Column(db.String(100), unique=True)
    location = db.Column(db.String(100))
    status = db.Column(db.String(20), default="Active")

    team_id = db.Column(db.Integer, db.ForeignKey("maintenance_team.id"))
