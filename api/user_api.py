from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from data.database_manager import get_db
from user_management import user_service
from security.encryption_service import verify_password
from security.auth_manager import create_access_token, verify_token
from pydantic import BaseModel

router = APIRouter(prefix="/users", tags=["Users"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="users/login")

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, user.model_dump())

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = user_service.get_user_by_username(db, form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username, "role": user.role})
    return {"access_token": access_token, "token_type": "bearer"}

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = verify_token(token)
    user = user_service.get_user_by_username(db, payload["username"])
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/me")
def read_users_me(current_user: dict = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "username": current_user.username, 
        "email": current_user.email, 
        "balance": current_user.balance, 
        "role": current_user.role
    }
