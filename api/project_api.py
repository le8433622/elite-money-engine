from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from data.database_manager import get_db
from data.models import MemberProject, User
from api.user_api import get_current_user
from ai_integration.ai_core import ai_optimizer
from pydantic import BaseModel

router = APIRouter(prefix="/social", tags=["Social Money Network"])

class ProjectCreate(BaseModel):
    title: str
    description: str

@router.post("/projects")
def create_project(project: ProjectCreate, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    """User đăng dự án lên Mạng Xã Hội Kiếm Tiền"""
    # Supreme AI nhúng tay định hướng ngay khi dự án hình thành
    ai_plan = ai_optimizer.supreme_commander_optimize_project(project.title, project.description)
    
    new_project = MemberProject(
        author_id=current_user.id,
        title=project.title,
        description=project.description,
        ai_optimization_plan=ai_plan
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Dự án đã được đưa lên Mạng lưới. Supreme Commander AI đã tiếp quản và Tối ưu hóa chiến lược!",
        "project_id": new_project.id,
        "ai_strategy": ai_plan
    }

@router.get("/projects")
def get_all_projects(db: Session = Depends(get_db)):
    """Xem Bản tin (News Feed) Mạng Xã Hội: Nơi các Dự Án sinh tiền thời gian thực"""
    projects = db.query(MemberProject).all()
    feed = []
    for p in projects:
        author = db.query(User).filter(User.id == p.author_id).first()
        author_name = author.username if author else "Unknown"
        feed.append({
            "id": p.id,
            "author": author_name,
            "title": p.title,
            "description": p.description,
            "revenue": float(p.total_revenue),
            "ai_plan": p.ai_optimization_plan
        })
    return {"projects": feed}
