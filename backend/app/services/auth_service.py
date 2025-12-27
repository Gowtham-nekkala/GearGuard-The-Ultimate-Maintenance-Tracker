from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.users import User

def register_user(data):
    user = User(
        username=data["username"],
        email=data["email"],
        password_hash=generate_password_hash(data["password"]),
        role=data.get("role", "user")
    )
    db.session.add(user)
    db.session.commit()
    return user
