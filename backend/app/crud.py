from sqlalchemy.orm import Session
from . import models, schemas

def create_meal(db: Session, meal_in: schemas.MealCreate):
    ingredients = db.query(models.Ingredient) \
        .filter(models.Ingredient.id.in_(meal_in.ingredient_ids)) \
        .all()
    db_meal = models.Meal(
        name=meal_in.name,
        description=meal_in.description,
        calories=meal_in.calories,
        instructions=meal_in.instructions,
        ingredients=ingredients
    )
    db.add(db_meal)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def update_meal(db: Session, meal_id: int, meal_in: schemas.MealCreate):
    db_meal = db.query(models.Meal).get(meal_id)
    if not db_meal:
        return None
    for field, value in meal_in.dict(exclude_unset=True).items():
        if field == "ingredient_ids":
            db_meal.ingredients = db.query(models.Ingredient) \
                .filter(models.Ingredient.id.in_(value)) \
                .all()
        else:
            setattr(db_meal, field, value)
    db.commit()
    db.refresh(db_meal)
    return db_meal

def get_meals_by_ingredient(db: Session, ingredient_name: str):
    return db.query(models.Meal) \
        .join(models.Meal.ingredients) \
        .filter(models.Ingredient.name == ingredient_name) \
        .all()

def get_ingredients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Ingredient).offset(skip).limit(limit).all()
