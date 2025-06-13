"""Add age, birthdate and is_active
Revision ID: 088debcb9f01
Revises: 64fec890be11
Create Date: 2025-06-12 13:35:11.268707

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
# revision identifiers, used by Alembic.
revision: str = '088debcb9f01'
down_revision: Union[str, None] = '64fec890be11'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('users', sa.Column('birthdate', sa.Date(), nullable=True))
    op.add_column('users', sa.Column('is_active', sa.Integer(), nullable=False, server_default='1'))

def downgrade() -> None:
    op.drop_column('users', 'is_active')
    op.drop_column('users', 'birthdate')
