import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy import Integer, String, Column, ForeignKey
from src.database import  Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class UserTg(Base):
    __tablename__ = "usertg"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    tg_id = Column(Integer, nullable=False)