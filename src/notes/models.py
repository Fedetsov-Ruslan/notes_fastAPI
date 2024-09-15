import datetime

from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from src.database import Base
from src.auth.models import User

# from src.database import metadata

class Record(Base):
    __tablename__ = "record"

    id = Column(Integer, primary_key=True)
    auther = Column(Integer, ForeignKey("user.id"), nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)
    updated_at = Column(TIMESTAMP, default=datetime.datetime.utcnow)


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    tag_name = Column(String, nullable=False)


class TagsRecord(Base):
    __tablename__ = "tagsrecord"

    id = Column(Integer, primary_key=True)
    tag_id = Column(Integer, ForeignKey("tags.id"), nullable=False)
    record_id = Column(Integer, ForeignKey("record.id"), nullable=False)

