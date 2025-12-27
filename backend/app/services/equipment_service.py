from app.extensions import db
from app.models.equipment import Equipment

def create_equipment(data):
    equipment = Equipment(
        name=data["name"],
        serial_number=data.get("serial_number"),
        location=data.get("location"),
        team_id=data.get("team_id"),
        assigned_to=data.get("assigned_to"),
        purchase_date=data.get("purchase_date"),
        equipment_type=data.get("equipment_type"),
        status="Active"
    )

    db.session.add(equipment)
    db.session.commit()
    return equipment


def get_all_equipment():
    return Equipment.query.all()


def get_equipment_by_id(equipment_id):
    return Equipment.query.get_or_404(equipment_id)
