from pydantic import BaseModel
from datetime import datetime


class RecordCreate(BaseModel):
    id: int
    auther: int
    title: str
    content: str    
    tags: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
        
