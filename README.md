# Elite Money Engine

Elite Money Engine là backend MVP cho bài toán quản lý tài chính cá nhân hoặc nhóm có hỗ trợ AI. Dự án tập trung vào một lõi rõ ràng: quản lý người dùng, giao dịch thu chi, tổng quan dòng tiền và gợi ý hành động từ dữ liệu giao dịch.

## Mục tiêu

- Xây backend API gọn, dễ mở rộng bằng FastAPI
- Quản lý người dùng với JWT authentication
- Ghi nhận giao dịch thu nhập và chi tiêu
- Tạo dashboard tổng quan tài chính
- Sinh gợi ý AI ở mức MVP từ dữ liệu giao dịch

## Phạm vi MVP

- Đăng ký tài khoản
- Đăng nhập, lấy access token
- Xem hồ sơ người dùng hiện tại
- Tạo và liệt kê giao dịch
- Xem tổng quan tài chính
- Nhận gợi ý chi tiêu và cảnh báo cơ bản

## Công nghệ

- FastAPI
- SQLAlchemy
- SQLite mặc định, PostgreSQL khi chạy qua Docker
- JWT + Passlib
- Docker và Docker Compose

## Cấu trúc dự án

```text
.
├── app
│   ├── __init__.py
│   ├── advisor.py
│   ├── config.py
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── security.py
├── .env.example
├── .gitignore
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## Chạy local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

API sẽ chạy tại `http://localhost:8000`.

## Chạy bằng Docker

```bash
docker compose up --build
```

## Các endpoint chính

- `GET /health`
- `POST /auth/register`
- `POST /auth/login`
- `GET /users/me`
- `POST /transactions`
- `GET /transactions`
- `GET /dashboard/overview`
- `GET /dashboard/advice`

## Hướng mở rộng tiếp theo

- Refresh token
- Bộ lọc giao dịch theo ngày và category
- Báo cáo theo tháng
- Budget và savings goals
- Kết nối LLM thật để phân tích tài chính nâng cao
- Web frontend hoặc mobile client

## Ghi chú

README cũ đã được thay bằng tài liệu mới, bám đúng phạm vi MVP và mục tiêu thực thi.
