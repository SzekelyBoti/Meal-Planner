# backend/app/api/__init__.py

# This file makes `app/api` a Python package.

# Optional: import your routers here for convenience,
# so you can do `from app.api import ingredients, meals`

from .ingredients import router as ingredients_router
# If you have a meals.py under app/api, uncomment:
# from .meals      import router as meals_router

__all__ = [
    "ingredients_router",
    # "meals_router",
]
