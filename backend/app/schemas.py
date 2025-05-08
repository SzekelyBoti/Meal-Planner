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
    instructions: Optional[str] = None

class MealRead(MealBase):
    id: int
    ingredients: List[IngredientRead]
    instructions: Optional[str]
    class Config:
        orm_mode = True
        
class MealOut(MealBase):
    id: int
    ingredients: List[IngredientRead]

    class Config:
        orm_mode = True

class MealUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    calories: Optional[int] = None
    instructions: Optional[str] = None
    ingredient_ids: Optional[List[int]] = None