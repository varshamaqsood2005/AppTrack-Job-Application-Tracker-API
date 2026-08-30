from datetime import datetime, date
from typing import Optional
from pydantic import BaseModel, ConfigDict

class ApplicationBase(BaseModel):
    company: str
    role: str
    source: str
    status: str = "applied"
    remote: bool = False
    expected_salary: Optional[int] = None
    applied_on: date
    first_response_on: Optional[date] = None
    notes: Optional[str] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(BaseModel):
    company: Optional[str] = None
    role: Optional[str] = None
    source: Optional[str] = None
    status: Optional[str] = None
    remote: Optional[bool] = None
    expected_salary: Optional[int] = None
    applied_on: Optional[date] = None
    first_response_on: Optional[date] = None
    notes: Optional[str] = None

class ApplicationOut(ApplicationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)