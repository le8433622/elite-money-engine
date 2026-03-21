from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, Text, TIMESTAMP
from sqlalchemy.orm import relationship
from datetime import datetime
from .database_manager import Base

# Mô hình User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    role = Column(String, default='user')
    balance = Column(DECIMAL, default=0.0)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)

    projects = relationship("Project", back_populates="owner")
    transactions = relationship("Transaction", back_populates="user")

# Mô hình Project
class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.utcnow)

    owner = relationship("User", back_populates="projects")

# Mô hình Transaction
class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(DECIMAL)
    type = Column(String)
    description = Column(Text)
    user_id = Column(Integer, ForeignKey('users.id'))
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

    user = relationship("User", back_populates="transactions")

# Mô hình AI Model
class AIModel(Base):
    __tablename__ = 'ai_models'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text)
    version = Column(String)
    accuracy = Column(DECIMAL)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

# Mô hình Log
class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(Text)
    level = Column(String)
    timestamp = Column(TIMESTAMP, default=datetime.utcnow)

# Kho Bạc Admin (Hút máu user)
class SystemWallet(Base):
    __tablename__ = 'system_wallet'

    id = Column(Integer, primary_key=True, index=True)
    total_revenue = Column(DECIMAL, default=0.0)
    last_updated = Column(TIMESTAMP, default=datetime.utcnow, onupdate=datetime.utcnow)

# AI OS Agents: Công cụ kiếm tiền siêu tỷ phú
class AutonomousAgent(Base):
    __tablename__ = 'autonomous_agents'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    niche = Column(String)           # Lĩnh vực (Crypto, Dropship...)
    capital_allocated = Column(DECIMAL, default=0.0) # Vốn Admin cấp
    total_roi_generated = Column(DECIMAL, default=0.0)
    status = Column(String, default="active") # active, dead
    created_at = Column(TIMESTAMP, default=datetime.utcnow)

# Mạng Xã Hội Kiếm Tiền: Dự Án Của Thành Viên
class MemberProject(Base):
    __tablename__ = 'member_projects'

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, index=True)  # ID của user tạo dự án
    title = Column(String, index=True)
    description = Column(String)
    ai_optimization_plan = Column(String, default="Chờ Supreme Commander phân tích...") # Gemini tối ưu
    total_revenue = Column(DECIMAL, default=0.0) # Lợi nhuận sinh ra
    status = Column(String, default="running") # running, completed
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
