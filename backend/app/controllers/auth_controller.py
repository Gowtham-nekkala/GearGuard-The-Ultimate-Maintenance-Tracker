from app.services.auth_service import register_user

def signup(data):
    return register_user(data)
