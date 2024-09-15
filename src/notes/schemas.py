from pydantic import BaseModel
from datetime import datetime


class RecordSchema(BaseModel):
    id: int
    auther: int
    title: str
    content: str    
    tags: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
