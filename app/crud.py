from typing import Sequence, Optional
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models import Application
from app.schemas import ApplicationCreate, ApplicationUpdate

def get_application(db: Session, app_id: int) -> Optional[Application]:
    return db.scalar(select(Application).where(Application.id == app_id))

def get_applications(db: Session) -> Sequence[Application]:
    return db.scalars(select(Application)).all()

def create_application(db: Session, app_in: ApplicationCreate) -> Application:
    db_obj = Application(**app_in.model_dump())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_application(db: Session, db_obj: Application, app_in: ApplicationUpdate) -> Application:
    # exclude_unset=True ensures PATCH only updates fields explicitly sent in the request
    update_data = app_in.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(db_obj, field, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_application(db: Session, db_obj: Application) -> None:
    db.delete(db_obj)
    db.commit()

from sqlalchemy import func

def get_status_counts(db: Session):
    results = (
        db.query(Application.status, func.count(Application.id))
        .group_by(Application.status)
        .all()
    )
    return {status: count for status, count in results}

def get_conversion_rate(db: Session):
    total = db.query(Application).count()
    if total == 0:
        return {"total_applications": 0, "offers": 0, "conversion_rate": 0.0}
    
    offers = db.query(Application).filter(Application.status == "offer").count()
    rate = round((offers / total) * 100, 2)
    return {
        "total_applications": total,
        "offers": offers,
        "conversion_rate": rate
    }