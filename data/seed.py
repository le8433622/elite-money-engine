import sys
from decimal import Decimal
from sqlalchemy.orm import Session
from data.database_manager import engine, SessionLocal, Base
from data.models import User, SystemWallet, AutonomousAgent, MemberProject
from security.encryption_service import get_password_hash

# Đảm bảo tạo bảng Database
Base.metadata.create_all(bind=engine)

def seed_data():
    db = SessionLocal()
    
    # Tạo Admin
    admin = db.query(User).filter(User.username == "admin_vip").first()
    if not admin:
        admin = User(
            username="admin_vip",
            email="admin@moneysystem.com",
            password_hash=get_password_hash("sieukiemtien"),
            role="admin",
            balance=Decimal("0.0")
        )
        db.add(admin)
    
    # Tạo Nhóm Công Dân (Quần chúng) để thực thi Vua Chúa Board
    for i in range(1, 6):
        user = db.query(User).filter(User.username == f"investor_{i}").first()
        if not user:
            user = User(
                username=f"investor_{i}",
                email=f"investor{i}@moneysystem.com",
                password_hash=get_password_hash("123456"),
                role="user",
                balance=Decimal("1000000.0") # Mỗi người 1 triệu USD
            )
            db.add(user)
            db.commit()
            db.refresh(user)
            
            # Tạo Luôn Dự án sinh lời nộp phế
            project = db.query(MemberProject).filter(MemberProject.title == f"Web3 Project Alpha by {user.username}").first()
            if not project:
                proj = MemberProject(
                    author_id=user.id,
                    title=f"Web3 DeFi Protocol by {user.username}",
                    description="Liquidity bootstrapping and AI-driven yield generation ecosystem.",
                    ai_optimization_plan="[Nexus SC] Deploying targeted community nodes, optimizing Layer-2 liquidity and executing strategic repurchases.",
                    total_revenue=Decimal("0.0")
                )
                db.add(proj)
            
    # Tạo SystemWallet làm lỗ đen hút tiền
    wallet = db.query(SystemWallet).first()
    if not wallet:
        wallet = SystemWallet(total_revenue=Decimal("0.0"))
        db.add(wallet)
        
    db.commit()
    print("MÔ PHỎNG HOÀN TẤT: Đã gieo mầm Admin VIP và 5 nạn nhân với số vốn khủng để hệ thống hoạt động!")

if __name__ == "__main__":
    seed_data()
