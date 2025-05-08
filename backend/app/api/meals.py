from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter(prefix="/api/meals", tags=["meals"])

@router.get("/", response_model=list[schemas.MealRead])
def read_meals(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_meals(db, skip, limit)