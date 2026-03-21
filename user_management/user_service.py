from sqlalchemy.orm import Session
from data.models import User
from security.encryption_service import get_password_hash
from fastapi import HTTPException

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user_data: dict):
    if get_user_by_username(db, user_data["username"]):
        raise HTTPException(status_code=400, detail="Username already registered")
    if get_user_by_email(db, user_data["email"]):
        raise HTTPException(status_code=400, detail="Email already registered")
        
    hashed_password = get_password_hash(user_data["password"])
    db_user = User(
        username=user_data["username"],
        email=user_data["email"],
        password_hash=hashed_password,
        role=user_data.get("role", "user")
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
