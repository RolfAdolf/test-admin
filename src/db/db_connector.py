from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from typing import AsyncGenerator

from core.settings import db_settings


engine = create_async_engine(db_settings.async_connection_string)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session
