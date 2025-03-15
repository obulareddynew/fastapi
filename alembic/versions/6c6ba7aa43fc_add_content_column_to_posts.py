"""add content column to posts

Revision ID: 6c6ba7aa43fc
Revises: 3208ebd50e75
Create Date: 2025-03-14 18:36:31.935409

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6c6ba7aa43fc'
down_revision: Union[str, None] = '3208ebd50e75'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column('posts','content')
    pass
