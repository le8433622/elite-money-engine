import logging
import sys

# Tạo custom logger cho toàn hệ thống
logger = logging.getLogger("MoneySystem")
logger.setLevel(logging.INFO)

# Formatter
formatter = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# StreamHandler (Xuất ra console)
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

def get_logger(module_name: str):
    return logger.getChild(module_name)
