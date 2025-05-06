"""Add ingredients & instructions

Revision ID: b4d97cfaf346
Revises: ca387d9f4c05
Create Date: 2025-05-06 11:00:42.277357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4d97cfaf346'
down_revision: Union[str, None] = 'ca387d9f4c05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
