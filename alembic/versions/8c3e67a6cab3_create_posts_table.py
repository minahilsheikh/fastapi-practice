"""create posts table

Revision ID: 8c3e67a6cab3
Revises: 
Create Date: 2025-01-14 10:59:39.887439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c3e67a6cab3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    #access op object from 
    #sa - sqlalchemy 
    op.create_table("posts", sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
                    sa.Column('title', sa.String(), nullable=False))
 

def downgrade() -> None:
    #how do we undo these changes 
    op.drop_table("posts")
