"""empty message

Revision ID: 90d058421364
Revises: 
Create Date: 2023-11-21 22:25:42.203196

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '90d058421364'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), nullable=False),
    sa.Column('bio', sa.VARCHAR(length=255), nullable=False),
    sa.Column('profile_picture', sa.String(), nullable=False),
    sa.Column('gender', sa.VARCHAR(length=255), nullable=True),
    sa.Column('birthdate', sa.Date(), nullable=True),
    sa.Column('is_verified', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_writer', sa.Boolean(), nullable=True),
    sa.Column('registration_date', sa.DateTime(timezone=True), nullable=True),
    sa.PrimaryKeyConstraint('user_id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
