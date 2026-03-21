from core_system.logging import get_logger
from fastapi import HTTPException

logger = get_logger("gps_service")

# Vùng an toàn (Bounding box của Việt Nam)
ALLOWED_REGION = {
    "lat_min": 8.0,
    "lat_max": 23.39,
    "long_min": 102.14,
    "long_max": 109.46
}

def verify_transaction_location(lat: float, long: float, amount: float):
    # Những giao dịch lớn yêu cầu xác minh vị trí nghiêm ngặt
    if amount > 1000000:
        if not (ALLOWED_REGION["lat_min"] <= lat <= ALLOWED_REGION["lat_max"] 
                and ALLOWED_REGION["long_min"] <= long <= ALLOWED_REGION["long_max"]):
            logger.warning(f"Cảnh báo bảo mật: Giao dịch lớn từ địa điểm nghi vấn (Lat: {lat}, Long: {long})")
            raise HTTPException(status_code=403, detail="Giao dịch lớn bị khóa do thực hiện tại không gian địa lý không xác thực theo lệnh hệ thống siêu kiếm tiền.")
    logger.info("Xác thực GPS giao dịch thành công. Luồng tiền an toàn.")
    return True
