from pydantic import BaseModel
from typing import Optional

class MealBase(BaseModel):
    name: str
    description: Optional[str] = None
    calories: Optional[int] = None

class MealCreate(MealBase):
    pass

class MealUpdate(MealBase):
    pass

class MealOut(MealBase):
    id: int

    class Config:
        orm_mode = True
