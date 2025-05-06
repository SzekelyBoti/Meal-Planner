from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.app import crud, schemas, database

router = APIRouter(prefix="/api/ingredients", tags=["ingredients"])

@router.get("/", response_model=list[schemas.IngredientRead])
def read_ingredients(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_ingredients(db, skip, limit)
