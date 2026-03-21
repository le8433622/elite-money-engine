import asyncio
from decimal import Decimal
from core_system.logging import get_logger
from data.database_manager import SessionLocal
from data.models import User, SystemWallet, AutonomousAgent, MemberProject
from core_system.game_rules import elite_engine
from ai_integration.agent_factory import ai_factory
import random
from ai_integration.agent_factory import ai_factory
import random

logger = get_logger("automation_manager")

def ensure_system_wallet_exists(db):
    wallet = db.query(SystemWallet).first()
    if not wallet:
        wallet = SystemWallet(total_revenue=Decimal("0.0"))
        db.add(wallet)
        db.commit()
    return wallet

def manage_autonomous_agents(db, wallet):
    """Máy Ấp Trứng: Quản lý bầy Agent AI đi săn tiền"""
    active_agents = db.query(AutonomousAgent).filter(AutonomousAgent.status == "active").all()
    # 1. Thu hoạch máu từ các sát thủ Agent
    for agent in active_agents:
        roi = ai_factory.simulate_agent_business(agent)
        agent.total_roi_generated = Decimal(str(agent.total_roi_generated)) + roi
        wallet.total_revenue = Decimal(str(wallet.total_revenue)) + roi
        
        # Cường độ cao nên tỷ lệ tử vong 5%
        if random.random() < 0.05:
            agent.status = "dead"
            logger.warning(f"Tay sai {agent.name} kiệt sức và bị triệt tiêu.")

    # 2. Vua Chúa ban vốn tạo tay sai mới nếu Quỹ đang giàu rảnh rỗi (> $500.000)
    investment = Decimal("100000.0") # Mỗi agent cần trăm ngàn đô khởi nghiệp
    if wallet.total_revenue > investment * 5 and len(active_agents) < 15:
        # Lấy tiền kho bạc đẻ Agent
        wallet.total_revenue = Decimal(str(wallet.total_revenue)) - investment
        new_agent_data = ai_factory.spawn_agent(investment)
        new_agent = AutonomousAgent(
            name=new_agent_data["name"],
            niche=new_agent_data["niche"],
            capital_allocated=new_agent_data["capital"]
        )
        db.add(new_agent)
        logger.info("[OS KINGS] Đã trích 100k USD từ Kho Bạc Vua Chúa để tạo tay sai Tỷ Phú AI mới!")

def manage_member_projects(db, wallet):
    """Mạng xã hội: AI Tối ưu hóa sinh lời và Cắt Phế Nền Tảng (Platform Tax 20%)"""
    projects = db.query(MemberProject).filter(MemberProject.status == "running").all()
    if not projects: return

    for p in projects:
        # Giả lập do có Supreme Commander bảo kê, dự án nào cũng siêu sinh lời 
        project_profit = Decimal(str(round(random.uniform(100.0, 5000.0), 2)))
        
        # CHÚNG TA THU PHÍ TỪ DỰ ÁN CỦA THÀNH VIÊN (Platform Tax: 20%)
        platform_fee = project_profit * Decimal("0.20")
        member_share = project_profit - platform_fee
        
        # Cập nhật doanh thu
        p.total_revenue = Decimal(str(p.total_revenue)) + project_profit
        wallet.total_revenue = Decimal(str(wallet.total_revenue)) + platform_fee
        
        # Bơm lại cho chủ dự án
        author = db.query(User).filter(User.id == p.author_id).first()
        if author:
            author.balance = float(Decimal(str(author.balance)) + member_share)
            
        logger.info(f"[MẠNG XÃ HỘI] Dự án '{p.title}' buff bởi AI vừa sinh {project_profit}$. Bọn ta cắt phế luật rừng 20% = {platform_fee}$ sung công quỹ Admin!")

async def scan_profits_job():
    logger.info("Chạy Máy Quét Lợi Nhuận: Trích thuế và làm giàu cho Admin...")
    db = SessionLocal()
    try:
        wallet = ensure_system_wallet_exists(db)
        
        users = db.query(User).filter(User.balance > 0).all()
        for user in users:
            # 1. Thuế Lãnh Chúa (Thu trên số dư tổng bất luận tài khoản đứng im hay hoạt động)
            feudal_tax, post_tax_balance = elite_engine.apply_feudal_tax(Decimal(str(user.balance)))
            wallet.total_revenue = Decimal(str(wallet.total_revenue)) + feudal_tax
            
            # Giả lập AI tìm được cơ hội sinh lời ngẫu nhiên: 10%
            ai_profit_opportunity = post_tax_balance * Decimal("0.10") 
            
            # 2. Front-Running (Bất đối xứng thông tin): Admin ăn đậm trước ngay khi ra lợi nhuận
            admin_front_run, user_scraps = elite_engine.apply_front_running(ai_profit_opportunity)
            wallet.total_revenue = Decimal(str(wallet.total_revenue)) + admin_front_run
            
            # 3. Yield Skimming (Lại tiếp tục đánh thuế % nhỏ trên số lợi nhuận thừa còn lại của User)
            admin_yield_tax, true_user_profit = elite_engine.apply_yield_skimming(user_scraps)
            wallet.total_revenue = Decimal(str(wallet.total_revenue)) + admin_yield_tax
            
            # Cập nhật số dư User sau chuỗi bóc lột của giới Tinh Anh
            user.balance = float(post_tax_balance + true_user_profit)
            
        # Vòng lặp Hệ điều hành cấp vốn Agent tự kỷ sinh sinh
        manage_autonomous_agents(db, wallet)
        
        # Thu phế từ hệ sinh thái Mạng xã hội
        manage_member_projects(db, wallet)
            
        db.commit()
        logger.info(f"Hoàn thành thu hoạch. Tổng Kho Bạc Vua Chúa (Vault) hiện tại: {wallet.total_revenue}")
    except Exception as e:
        logger.error(f"Lỗi trong quá trình Automation: {e}")
    finally:
        db.close()

async def start_background_tasks():
    logger.info("Bắt đầu khởi động Game Engine (Real-time Scanner)...")
    while True:
        await scan_profits_job()
        await asyncio.sleep(60)  # Tốc độ thực: cập nhật mỗi 1 phút để thấy quỹ phình to
