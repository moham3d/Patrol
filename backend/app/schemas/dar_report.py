from pydantic import BaseModel
from datetime import datetime

class DARReportBase(BaseModel):
    content: str

class DARReportCreate(DARReportBase):
    pass

class DARReport(DARReportBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
