"""add content column to posts table

Revision ID: 186858884190
Revises: 8c3e67a6cab3
Create Date: 2025-01-15 12:16:10.034836

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '186858884190'
down_revision: Union[str, None] = '8c3e67a6cab3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))



def downgrade() -> None:
    op.drop_column('posts', 'content')
