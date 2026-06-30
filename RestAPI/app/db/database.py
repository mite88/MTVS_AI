# app/db/database.py

from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine
from app.core.config import get_settings

engine:AsyncEngine = create_async_engine(
    url=get_settings.db_url,
    echo=False, # 로그
    pool_pre_ping = True,
    pool_size = 5,
    max_overflow = 10,
)

