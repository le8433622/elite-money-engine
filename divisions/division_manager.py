from core_system.logging import get_logger

logger = get_logger("divisions")

class DivisionManager:
    """Hệ thống tự động phân nhánh dòng tiền thành các quỹ nhỏ theo AI điều phối."""
    def __init__(self):
        self.divisions = {}
        
    def create_division(self, user_id: int, funds: float, division_type: str = "nhất_phân"):
        div_id = len(self.divisions) + 1
        self.divisions[div_id] = {
            "user_id": user_id,
            "funds": funds,
            "type": division_type,
            "status": "active"
        }
        logger.info(f"Đã tạo nhánh (Thuộc Địa) '{division_type}' (ID: {div_id}) cho User {user_id} với ngân sách {funds}")
        return div_id

    def extract_tribute(self, from_division_id: int):
        """Mô hình Vua Chúa: Lấy cống nạp từ các thuộc địa nhánh phụ lên đỉnh kim tự tháp."""
        division = self.divisions.get(from_division_id)
        if division and division["funds"] > 0:
            extracted = division["funds"] * 0.15 # Hút 15% quỹ của thuộc địa làm cống nạp
            division["funds"] -= extracted
            logger.info(f"[KIM TỰ THÁP TÀI SẢN] Hút sinh lực {extracted} làm cống nạp từ Chi nhánh {from_division_id}.")
            return extracted
        return 0

division_mgr = DivisionManager()
