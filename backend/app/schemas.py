from pydantic import BaseModel
from typing import List, Optional

class IngredientBase(BaseModel):
    name: str

class IngredientRead(IngredientBase):
    id: int
    class Config:
        orm_mode = True

class MealBase(BaseModel):
    name: str
    description: Optional[str] = None
    calories: Optional[int] = None
    instructions: Optional[str] = None

class MealCreate(MealBase):
    ingredient_ids: List[int] = []

class MealRead(MealBase):
    id: int
    ingredients: List[IngredientRead]
    class Config:
        orm_mode = True
