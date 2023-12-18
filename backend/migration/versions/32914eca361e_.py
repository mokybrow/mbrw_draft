"""empty message

Revision ID: 32914eca361e
Revises: 73010552f8d8
Create Date: 2023-12-18 23:27:42.775406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '32914eca361e'
down_revision: Union[str, None] = '73010552f8d8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comments', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('friends', 'follower_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('friends', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_genres', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_genres', 'genre_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_platforms', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_platforms', 'platform_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_reviews', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('game_reviews', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('games_age_ratings', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('games_age_ratings', 'age_rating_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('list_games', 'list_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('list_games', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('post_pictures', 'post_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('post_tags', 'post_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('post_tags', 'tag_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('posts', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('posts', 'wall_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('posts', 'parent_post_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('profile_pictures', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_favorite', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_favorite', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_games', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_games', 'game_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_games', 'activity_id',
               existing_type=sa.UUID(),
               nullable=False)
    op.alter_column('user_lists', 'user_id',
               existing_type=sa.UUID(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_lists', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('user_games', 'activity_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('user_games', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('user_games', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('user_favorite', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('user_favorite', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('profile_pictures', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('posts', 'parent_post_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('posts', 'wall_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('posts', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('post_tags', 'tag_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('post_tags', 'post_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('post_pictures', 'post_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('list_games', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('list_games', 'list_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('games_age_ratings', 'age_rating_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('games_age_ratings', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_reviews', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_reviews', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_platforms', 'platform_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_platforms', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_genres', 'genre_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('game_genres', 'game_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('friends', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('friends', 'follower_id',
               existing_type=sa.UUID(),
               nullable=True)
    op.alter_column('comments', 'user_id',
               existing_type=sa.UUID(),
               nullable=True)
    # ### end Alembic commands ###
