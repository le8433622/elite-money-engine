from core_system.logging import get_logger

logger = get_logger("communications")

def send_notification(user_id: int, message: str):
    """
    Giả lập gửi PUSH NOTIFICATION đến thiết bị di động của User hoặc Admin.
    """
    logger.info(f"[PUSH NOTIFIED - User {user_id}]: {message}")
    return True
