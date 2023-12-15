from typing import Optional
from fastapi import (
    APIRouter,
    Depends,
)
from fastapi.responses import FileResponse
from pydantic import UUID4
from sqlalchemy.ext.asyncio import AsyncSession
from dudesplay_api.integrations.get_filters import get_filters_bd, normilize

from dudesplay_api.database import get_async_session


router = APIRouter(
    prefix='/exp',
    tags=['exp'],
)


@router.get(
    '/db-filter-test', description='Получение фото профиля пользователя по id',
)
async def get_db_filters(
    genre: str | None , platform: Optional[str] = None, db: AsyncSession = Depends(get_async_session),
):
    user_img = await get_filters_bd(db=db, genre=genre, platform=platform)
    print(user_img)
    return None


@router.get('/normix_data')
async def normilize_data(db: AsyncSession = Depends(get_async_session)):
    await normilize(db=db)
    return None