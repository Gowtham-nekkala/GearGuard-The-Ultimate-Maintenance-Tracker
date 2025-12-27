from app.services.equipment_service import (
    create_equipment as create_equipment_service,
    get_all_equipment as get_all_equipment_service,
    get_equipment_by_id as get_equipment_by_id_service
)

def create_equipment(data):
    equipment = create_equipment_service(data)
    return equipment

def get_all_equipment():
    equipments = get_all_equipment_service()

    return [
        {
            "id": e.id,
            "name": e.name,
            "serial_number": e.serial_number,
            "location": e.location,
            "status": e.status,
            "team_id": e.team_id,
            "assigned_to": e.assigned_to,
            "purchase_date": e.purchase_date,
            "equipment_type": e.equipment_type
        }
        for e in equipments
    ]

def get_equipment_by_id(equipment_id):
    e = get_equipment_by_id_service(equipment_id)

    return {
        "id": e.id,
        "name": e.name,
        "serial_number": e.serial_number,
        "location": e.location,
        "status": e.status,
        "team_id": e.team_id,
        "assigned_to": e.assigned_to,
        "purchase_date": e.purchase_date,
        "equipment_type": e.equipment_type
    }