from typing import Optional

from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_async_session
from api.integrations.get_filters import game_parser, get_filters_bd, norm_data

router = APIRouter(
    prefix='/exp',
    tags=['exp'],
)


@router.get(
    '/db-filter-test',
    description='Получение фото профиля пользователя по id',
)
async def get_db_filters(
    genre: str | None,
    platform: Optional[str] = None,
    db: AsyncSession = Depends(get_async_session),
):
    user_img = await get_filters_bd(db=db, genre=genre, platform=platform)
    print(user_img)
    return None


@router.get('/admin/game_parser')
async def parse_games(
    db: AsyncSession = Depends(get_async_session),
):
    await game_parser(db=db)


@router.get('/normilize_data')
async def normilize_data(db: AsyncSession = Depends(get_async_session)):
    await norm_data(db=db)
    return None
