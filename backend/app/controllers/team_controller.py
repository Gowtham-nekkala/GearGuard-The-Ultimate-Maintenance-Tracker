from app.services.team_service import (
    create_team as create_team_service,
    get_all_teams as get_all_teams_service
)

def create_team(data):
    team = create_team_service(data)
    return team


def get_all_teams():
    teams = get_all_teams_service()

    return [
        {
            "id": t.id,
            "name": t.name,
            "description": t.description
        }
        for t in teams
    ]