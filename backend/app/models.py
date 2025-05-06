from sqlalchemy import (
    Table, Column, Integer, String, Text, ForeignKey
)
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

meal_ingredient = Table(
    "meal_ingredient",
    Base.metadata,
    Column("meal_id", Integer, ForeignKey("meals.id"), primary_key=True),
    Column("ingredient_id", Integer, ForeignKey("ingredients.id"), primary_key=True),
)

class Meal(Base):
    __tablename__ = "meals"
    id           = Column(Integer, primary_key=True, index=True)
    name         = Column(String(100), nullable=False)
    description  = Column(Text, nullable=True)
    calories     = Column(Integer, nullable=True)
    instructions = Column(Text, nullable=True) 

    ingredients = relationship(
        "Ingredient",
        secondary=meal_ingredient,
        back_populates="meals",
    )

class Ingredient(Base):
    __tablename__ = "ingredients"
    id    = Column(Integer, primary_key=True, index=True)
    name  = Column(String(50), unique=True, nullable=False)

    meals = relationship(
        "Meal",
        secondary=meal_ingredient,
        back_populates="ingredients",
    )
