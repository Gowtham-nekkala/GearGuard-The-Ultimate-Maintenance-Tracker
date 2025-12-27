from app.models.equipment import Equipment

def auto_assign_team(equipment_id):
    equipment = Equipment.query.get(equipment_id)
    return equipment.team_id if equipment else None
