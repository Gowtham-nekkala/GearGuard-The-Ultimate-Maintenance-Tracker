from app.models.equipment import Equipment
from app.models.employee import Employee

def auto_assign_team(equipment_id):
    """
    Returns the maintenance team assigned to the equipment.
    """
    equipment = Equipment.query.get(equipment_id)
    if not equipment:
        return None
    return equipment.team_id


def get_team_members(team_id):
    """
    Returns all employees belonging to a maintenance team.
    """
    return Employee.query.filter_by(team_id=team_id).all()
