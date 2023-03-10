# Database

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker

from core.configs import settings

# Módulo interno


engine: AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncSession = sessionmaker(
    autocommit=False,
    expire_on_commit=False,
    autoflush=False,
    class_=AsyncSession,
    bind=engine,
)
