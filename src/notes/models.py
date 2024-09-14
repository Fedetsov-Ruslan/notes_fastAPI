import datetime

from sqlalchemy import Table, Integer, String, Column, TIMESTAMP, Boolean, ForeignKey
from sqlalchemy.orm import DeclarativeMeta, declarative_base

from src.database import metadata

Base: DeclarativeMeta = declarative_base()


record = Table(
    "record",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('auther', Integer, ForeignKey("user.id")),
    Column('title', String, nullable=False),
    Column('content', String, nullable=False),
    Column('tags', Integer, ForeignKey("tags.id")),
    Column('created_at', TIMESTAMP, default=datetime.datetime.utcnow),
    Column('updated_at', TIMESTAMP, default=datetime.datetime.utcnow),
)
tags = Table(
    "tags",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('tag_name', String, nullable=False),
)

tagsrecord = Table(
    "tagsrecord",
    metadata,
    Column("id", Integer, primary_key=True),
    Column('tag_id', Integer, ForeignKey("tags.id")),
    Column('record_id', Integer, ForeignKey("record.id")),
)