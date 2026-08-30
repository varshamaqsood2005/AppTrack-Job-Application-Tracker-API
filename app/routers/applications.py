from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db import get_db
from app import crud, schemas

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.get("", response_model=List[schemas.ApplicationOut])
def list_applications(db: Session = Depends(get_db)):
    return crud.get_applications(db)

@router.post("", response_model=schemas.ApplicationOut, status_code=status.HTTP_201_CREATED)
def create_application(payload: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    return crud.create_application(db, payload)

@router.get("/stats/status-counts")
def get_status_counts(db: Session = Depends(get_db)):
    return crud.get_status_counts(db)

@router.get("/stats/conversion-rate")
def get_conversion_rate(db: Session = Depends(get_db)):
    return crud.get_conversion_rate(db)

@router.get("/{app_id}", response_model=schemas.ApplicationOut)
def get_application(app_id: int, db: Session = Depends(get_db)):
    app_obj = crud.get_application(db, app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_obj

@router.patch("/{app_id}", response_model=schemas.ApplicationOut)
def update_application(app_id: int, payload: schemas.ApplicationUpdate, db: Session = Depends(get_db)):
    app_obj = crud.get_application(db, app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    return crud.update_application(db, app_obj, payload)

@router.delete("/{app_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_application(app_id: int, db: Session = Depends(get_db)):
    app_obj = crud.get_application(db, app_id)
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    crud.delete_application(db, app_obj)
    return None