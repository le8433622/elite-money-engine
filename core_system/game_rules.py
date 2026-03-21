from decimal import Decimal
from core_system.logging import get_logger

logger = get_logger("game_rules")

class GameRules:
    def __init__(self):
        # Admin luôn thắng: Tự động giữ % hoa hồng / thuế ẩn cho hệ thống
        self.TRANSACTION_SPREAD_FEE = Decimal("0.02")  # Thuế 2% nếu user giao dịch (nạp/rút)
        self.YIELD_SKIMMING_RATE = Decimal("0.06")     # Cắt phế 6% khi AI tạo ra dòng lời

    def apply_transaction_fee(self, amount: Decimal) -> (Decimal, Decimal):
        """Khấu trừ ngầm khi user luân chuyển vốn"""
        fee = amount * self.TRANSACTION_SPREAD_FEE
        net_amount = amount - fee
        logger.info(f"[HOUSE EDGE] Phí Spread: trích {fee} từ vốn {amount} của User")
        return fee, net_amount

    def apply_yield_skimming(self, profit: Decimal) -> (Decimal, Decimal):
        """Admin ăn chặn tiền lợi nhuận của User (Thuế ngầm hệ thống)"""
        skimmed = profit * self.YIELD_SKIMMING_RATE
        user_profit = profit - skimmed
        logger.info(f"[YIELD SKIMMING] Cắt lợi nhuận {skimmed} chuyển thẳng vào Kho bạc Admin.")
        return skimmed, user_profit

class EliteGameRules(GameRules):
    def __init__(self):
        super().__init__()
        # Kẻ mạnh ăn trước: Bất đối xứng thông tin
        self.FRONT_RUNNING_FEE = Decimal("0.30") # Admin ăn 30% tổng cơ hội siêu lợi nhuận của AI đầu tiên
        # Thuế Lãnh Chúa: Thuế tài sản cố định
        self.FEUDAL_TAX_RATE = Decimal("0.01")   # Định kỳ cắn 1% trên Tổng Tài Sản của user không lý do

    def apply_feudal_tax(self, user_balance: Decimal) -> (Decimal, Decimal):
        """Luật Vua Chúa: Trữ tiền trong hệ thống là phải đóng thuế bến bãi."""
        tax = user_balance * self.FEUDAL_TAX_RATE
        net_balance = user_balance - tax
        logger.info(f"[FEUDAL TAX] Vắt kiệt {tax} từ số dư {user_balance} của User (Mô hình Lãnh chúa).")
        return tax, net_balance

    def apply_front_running(self, ai_opportunity: Decimal) -> (Decimal, Decimal):
        """Kẻ có quyền sẽ đánh phủ đầu trước người yếu thông qua tín hiệu nội gián của AI"""
        admin_first_blood = ai_opportunity * self.FRONT_RUNNING_FEE
        user_scraps = ai_opportunity - admin_first_blood
        logger.info(f"[FRONT RUNNING] Tinh anh thâu tóm {admin_first_blood} trước, nhả lại {user_scraps} cho User đáy tháp.")
        return admin_first_blood, user_scraps

elite_engine = EliteGameRules()
