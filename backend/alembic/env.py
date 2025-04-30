import sys
from pathlib import Path

# Add the project's root directory to sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.models import Base

target_metadata = Base.metadata