"""empty message

Revision ID: 134828042d65
Revises: 90d058421364
Create Date: 2023-11-21 22:35:10.416176

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '134828042d65'
down_revision: Union[str, None] = '90d058421364'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('users', 'profile_picture',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'profile_picture',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'bio',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###
