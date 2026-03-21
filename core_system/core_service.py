from .logging import get_logger

logger = get_logger("core_service")

class CoreService:
    def __init__(self):
        self.is_running = False

    def start_system(self):
        logger.info("Khởi động MoneySystem Core Service...")
        self.is_running = True
        logger.info("MoneySystem chạy ở chế độ nền thành công.")

    def stop_system(self):
        logger.info("Dừng MoneySystem Core Service...")
        self.is_running = False

core_app = CoreService()
