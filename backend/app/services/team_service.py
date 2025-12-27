from app.extensions import db
from app.models.maintenance_team import MaintenanceTeam

def create_team(data):
    team = MaintenanceTeam(
        name=data["name"],
        description=data.get("description")
    )
    db.session.add(team)
    db.session.commit()
    return team


def get_all_teams():
    return MaintenanceTeam.query.all()
