from app.extensions import db

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120))
    designation = db.Column(db.String(50))
    phone = db.Column(db.String(20))
    address = db.Column(db.String(200))

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    team_id = db.Column(db.Integer, db.ForeignKey("maintenance_team.id"))
