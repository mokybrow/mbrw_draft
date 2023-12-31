"""empty message

Revision ID: 9cf8627b29ef
Revises: f79b11634475
Create Date: 2024-01-03 20:57:35.134190

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '9cf8627b29ef'
down_revision: Union[str, None] = 'f79b11634475'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('completed_count', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('wishlist_count', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('favorite_count', sa.Integer(), nullable=True))
    op.add_column('games', sa.Column('average_rating', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'average_rating')
    op.drop_column('games', 'favorite_count')
    op.drop_column('games', 'wishlist_count')
    op.drop_column('games', 'completed_count')
    # ### end Alembic commands ###
