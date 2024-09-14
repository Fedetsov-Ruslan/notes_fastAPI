from pydantic import BaseModel
from datetime import datetime


class RecordSchema(BaseModel):
    id: int
    auther: int
    content: str
    title: str
    tags: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True