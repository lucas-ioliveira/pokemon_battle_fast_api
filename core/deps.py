from typing import Generator

from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session


# Fechando a conexão


async def get_session() -> Generator:
    session: AsyncSession = Session()

    try:
        yield session
    finally:
        await session.close()
