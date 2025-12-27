from app.extensions import db

class MaintenanceTeam(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))

    members = db.relationship("Employee", backref="team")
