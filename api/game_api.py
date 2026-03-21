from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.database_manager import get_db
from data.models import SystemWallet
from api.user_api import get_current_user
from security.permission_manager import require_admin
import random

router = APIRouter(prefix="/game", tags=["Game Engine"])

fake_requests = [
    "System Alert: Requesting localized API limit expansion for Cross-Border Arbitrage deployment.",
    "High-Yield Opportunity: Detected Web3 Layer-2 liquidity imbalance. Requesting bridge allocation for Flash Loan execution.",
    "Strategic Update: New DeFi protocol listed. Recommending a deployment strategy meeting at 10 AM tomorrow to optimize yield farming.",
    "Resource Allocation: Sub-agent 'HFT Trader Alpha' requires increased credit facility to execute delta-neutral options strategies.",
    "Performance Report: Winrate holds at 99.8%. Proposing creation of a new autonomous cluster targeting emerging markets. Awaiting Authorization!"
]
active_chat_requests = []

@router.get("/admin-vault")
def get_admin_vault(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    require_admin({"role": current_user.role})
    wallet = db.query(SystemWallet).first()
    total = float(wallet.total_revenue) if wallet else 0.0
    return {
        "status": "Admin always wins",
        "total_revenue_collected": total,
        "message": "Aggregated platform fees and ecosystem yields successfully deposited."
    }

@router.get("/admin-requests")
def get_admin_requests(db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    require_admin({"role": current_user.role})
    global active_chat_requests
    # Random tỷ lệ có request mới từ Hệ Điều Hành liên tục
    if random.random() < 0.25 and len(active_chat_requests) < 3:
        active_chat_requests.append({
            "id": random.randint(10000, 99999), 
            "message": random.choice(fake_requests),
            "urgent": True
        })
    return {"requests": active_chat_requests}

@router.post("/admin-requests/{req_id}/approve")
def approve_request(req_id: int, current_user: dict = Depends(get_current_user)):
    require_admin({"role": current_user.role})
    global active_chat_requests
    active_chat_requests = [r for r in active_chat_requests if r["id"] != req_id]
    return {"message": "Administration Override: Resource Allocation Approved. Nexus AI continues to optimize yields."}
