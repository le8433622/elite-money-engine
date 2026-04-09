from datetime import datetime
from typing import Literal

from pydantic import BaseModel, EmailStr, Field


class HealthOut(BaseModel):
    status: str
    app: str


class UserCreate(BaseModel):
    full_name: str = Field(min_length=2, max_length=120)
    email: EmailStr
    password: str = Field(min_length=8, max_length=128)


class UserOut(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    created_at: datetime

    model_config = {"from_attributes": True}


class LoginIn(BaseModel):
    email: EmailStr
    password: str


class TokenOut(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TransactionCreate(BaseModel):
    type: Literal["income", "expense"]
    category: str = Field(min_length=2, max_length=80)
    amount: float = Field(gt=0)
    note: str | None = Field(default=None, max_length=255)


class TransactionOut(BaseModel):
    id: int
    type: str
    category: str
    amount: float
    note: str | None
    created_at: datetime

    model_config = {"from_attributes": True}


class OverviewOut(BaseModel):
    total_income: float
    total_expense: float
    balance: float
    transaction_count: int


class AdviceOut(BaseModel):
    headline: str
    insights: list[str]
