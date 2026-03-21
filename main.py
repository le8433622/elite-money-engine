from sqlalchemy.orm import Session
from data.database_manager import engine, Base, get_db
from data import models
from api import user_api, admin_api, ai_api, game_api
from fastapi.middleware.cors import CORSMiddleware

# Tạo bảng trong cơ sở dữ liệu
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MoneySystem API", description="Siêu hệ thống kiếm tiền", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_api.router)
app.include_router(admin_api.router)
app.include_router(ai_api.router)
app.include_router(game_api.router)
app.include_router(project_api.router)

@app.on_event("startup")
async def startup_event():
    import asyncio
    from automation.task_manager import start_background_tasks
    # Chạy vòng lặp tự động kiếm tiền ngầm
    asyncio.create_task(start_background_tasks())

@app.get("/")
def read_root():
    return {"message": "Welcome to MoneySystem API"}

@app.get("/health")
def health_check():
    return {"status": "ok"}
