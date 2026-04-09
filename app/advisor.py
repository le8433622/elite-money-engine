from collections import defaultdict

from app.models import Transaction


def build_advice(transactions: list[Transaction]) -> tuple[str, list[str]]:
    if not transactions:
        return (
            "Chưa có dữ liệu giao dịch",
            [
                "Hãy tạo ít nhất 5 giao dịch để hệ thống bắt đầu đưa ra gợi ý thực tế.",
                "Ưu tiên phân loại giao dịch theo category để tăng độ hữu ích của dashboard.",
            ],
        )

    income = sum(t.amount for t in transactions if t.type == "income")
    expense = sum(t.amount for t in transactions if t.type == "expense")

    by_category: dict[str, float] = defaultdict(float)
    for tx in transactions:
        if tx.type == "expense":
            by_category[tx.category] += tx.amount

    largest_category = max(by_category, key=by_category.get) if by_category else None
    largest_value = by_category.get(largest_category, 0.0) if largest_category else 0.0

    insights: list[str] = []

    if expense > income and income > 0:
        insights.append("Chi tiêu đang vượt thu nhập. Nên giảm tốc độ chi hoặc tăng nguồn thu ngắn hạn.")
    elif income > 0:
        savings_rate = max((income - expense) / income, 0.0)
        insights.append(f"Tỷ lệ giữ lại dòng tiền hiện tại khoảng {savings_rate:.0%}.")

    if largest_category:
        insights.append(
            f"Nhóm chi tiêu lớn nhất hiện tại là '{largest_category}' với tổng {largest_value:.2f}."
        )

    if len(by_category) >= 3:
        insights.append("Bạn đã có dữ liệu đủ để bắt đầu theo dõi ngân sách theo nhóm chi tiêu.")

    if not insights:
        insights.append("Dữ liệu hiện tại ổn định, hãy tiếp tục ghi nhận giao dịch đều đặn.")

    return "Gợi ý tài chính cho kỳ hiện tại", insights
