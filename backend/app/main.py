﻿from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud, database
from .api.ingredients import router as ingredients_router
#from .api.meals import router as meals_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Dependency
app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
)
app.include_router(ingredients_router) 
#app.include_router(meals_router)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")

@app.post("/api/meals/", response_model=schemas.MealOut)
def create_meal(meal: schemas.MealCreate, db: Session = Depends(get_db)):
    return crud.create_meal(db=db, meal_in=meal)

@app.get("/api/meals/", response_model=list[schemas.MealOut])
def read_meals(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_meals(db, skip=skip, limit=limit)

@app.get("/api/meals/{meal_id}", response_model=schemas.MealOut)
def read_meal(meal_id: int, db: Session = Depends(get_db)):
    db_meal = crud.get_meal(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal

@app.put("/api/meals/{meal_id}", response_model=schemas.MealOut)
def update_meal(meal_id: int, meal: schemas.MealUpdate, db: Session = Depends(get_db)):
    db_meal = crud.update_meal(db, meal_id=meal_id, meal_in=meal)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal

@app.delete("/api/meals/{meal_id}", response_model=schemas.MealOut)
def delete_meal(meal_id: int, db: Session = Depends(get_db)):
    db_meal = crud.delete_meal(db, meal_id=meal_id)
    if db_meal is None:
        raise HTTPException(status_code=404, detail="Meal not found")
    return db_meal
