from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from data.database_manager import get_db
from data.models import Transaction, User
from api.user_api import get_current_user
from ai_integration.ai_core import analyze_investment_opportunities

router = APIRouter(prefix="/ai", tags=["AI Integration"])

@router.get("/optimize-revenue")
def optimize_revenue(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    user_id = current_user.id
    
    # Lấy lịch sử giao dịch của user
    transactions = db.query(Transaction).filter(Transaction.user_id == user_id).all()
    tx_list = [{"amount": float(t.amount), "type": t.type, "desc": t.description} for t in transactions]
    
    if not tx_list:
        return {"message": "Không đủ dữ liệu giao dịch để AI cấu trúc tài chính.", "transactions_count": 0}
        
    analysis_result = analyze_investment_opportunities(tx_list)
    
    return {
        "user_id": user_id,
        "current_balance": float(current_user.balance or 0),
        "ai_recommendation": analysis_result
    }
