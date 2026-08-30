from datetime import datetime, date
from typing import Optional
from sqlalchemy import String, Integer, Boolean, Date, DateTime, Text, func
from sqlalchemy.orm import Mapped, mapped_column
from app.db import Base

class Application(Base):
    __tablename__ = "applications"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    company: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(120), nullable=False)
    source: Mapped[str] = mapped_column(String(40), nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="applied")
    remote: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    expected_salary: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)
    applied_on: Mapped[date] = mapped_column(Date, nullable=False)
    first_response_on: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    notes: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)