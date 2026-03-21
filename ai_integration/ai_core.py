import os
import json
import google.generativeai as genai
from core_system.logging import get_logger

logger = get_logger("ai_core")

# Cấu hình Gemini AI
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "DUMMY_KEY_FOR_TESTING")
genai.configure(api_key=GEMINI_API_KEY)

# Model configuration
try:
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    logger.warning(f"Lỗi khởi tạo Gemini Model. System will run in fallback mode. Error: {e}")
    model = None

def analyze_investment_opportunities(transactions: list):
    prompt = f"""
Bạn là một AI chuyên gia tối ưu hóa dòng tiền và tư vấn đầu tư siêu lợi nhuận.
Tôi có lịch sử giao dịch tài chính sau: {json.dumps(transactions)}

Dựa vào dữ liệu này, hãy:
1. Đánh giá tính rủi ro, dòng tiền.
2. Đề xuất các kênh tự động tái đầu tư (phân bổ % vốn).
3. Đưa ra dự đoán mức sinh lời 30 ngày tới.

Output DUY NHẤT dưới dạng JSON hợp lệ:
{{
   "risk_level": "Low/Medium/High",
   "recommended_allocations": {{"stock": 40, "crypto": 30, "savings": 30}},
   "expected_return_30d_percent": 15.5,
   "analysis_message": "lời khuyên sinh lời"
}}
"""
        return json.loads(text_resp)
    except Exception as e:
        logger.error(f"Lỗi khi AI phân tích đầu tư: {str(e)}")
        return {"error": str(e), "message": "Hệ thống AI hiện đang bận hoặc có lỗi, chưa thể tối ưu."}
