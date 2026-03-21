from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database_manager import get_db
from data.models import User
from api.user_api import get_current_user
from security.permission_manager import require_admin

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/users")
def get_all_users(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_admin({"role": current_user.role})
    users = db.query(User).all()
    return [{"id": u.id, "username": u.username, "email": u.email, "balance": u.balance, "role": u.role} for u in users]

@router.post("/users/{user_id}/add_balance")
def add_balance(user_id: int, amount: float, db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_admin({"role": current_user.role})
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Cộng dồn tiền sinh lời 
    user.balance = float(user.balance) + amount
    db.commit()
    db.refresh(user)
    return {"message": "Balance updated successfully", "new_balance": user.balance}
