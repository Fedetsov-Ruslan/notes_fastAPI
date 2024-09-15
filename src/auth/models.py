import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID
from sqlalchemy.orm import DeclarativeMeta, declarative_base
from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean
from src.database import metadata, Base

class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)