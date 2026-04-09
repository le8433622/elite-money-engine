from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy.orm import Session

from app.advisor import build_advice
from app.config import settings
from app.db import Base, engine, get_db
from app.models import Transaction, User
from app.schemas import (
    AdviceOut,
    HealthOut,
    LoginIn,
    OverviewOut,
    TokenOut,
    TransactionCreate,
    TransactionOut,
    UserCreate,
    UserOut,
)
from app.security import create_access_token, get_current_user, hash_password, verify_password


Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.app_name, version="1.0.0")


@app.get("/health", response_model=HealthOut)
def health_check():
    return {"status": "ok", "app": settings.app_name}


@app.post("/auth/register", response_model=UserOut, status_code=status.HTTP_201_CREATED)
def register(payload: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        full_name=payload.full_name,
        email=payload.email,
        password_hash=hash_password(payload.password),
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


@app.post("/auth/login", response_model=TokenOut)
def login(payload: LoginIn, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == payload.email).first()
    if user is None or not verify_password(payload.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = create_access_token(user.email)
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=UserOut)
def read_me(current_user: User = Depends(get_current_user)):
    return current_user


@app.post("/transactions", response_model=TransactionOut, status_code=status.HTTP_201_CREATED)
def create_transaction(
    payload: TransactionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transaction = Transaction(
        user_id=current_user.id,
        type=payload.type,
        category=payload.category,
        amount=payload.amount,
        note=payload.note,
    )
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction


@app.get("/transactions", response_model=list[TransactionOut])
def list_transactions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Transaction)
        .filter(Transaction.user_id == current_user.id)
        .order_by(Transaction.created_at.desc())
        .all()
    )


@app.get("/dashboard/overview", response_model=OverviewOut)
def overview(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transactions = db.query(Transaction).filter(Transaction.user_id == current_user.id).all()
    total_income = sum(t.amount for t in transactions if t.type == "income")
    total_expense = sum(t.amount for t in transactions if t.type == "expense")
    return {
        "total_income": total_income,
        "total_expense": total_expense,
        "balance": total_income - total_expense,
        "transaction_count": len(transactions),
    }


@app.get("/dashboard/advice", response_model=AdviceOut)
def advice(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    transactions = db.query(Transaction).filter(Transaction.user_id == current_user.id).all()
    headline, insights = build_advice(transactions)
    return {"headline": headline, "insights": insights}
