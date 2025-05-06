"""Add ingredients & instructions

Revision ID: 7f8ca7e8eff6
Revises: b4d97cfaf346
Create Date: 2025-05-06 16:02:51.366622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7f8ca7e8eff6'
down_revision: Union[str, None] = 'b4d97cfaf346'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
