import asyncio
import logging
from typing import AsyncGenerator
from sqlalchemy import exc
from sqlalchemy.ext.asyncio import (AsyncSession, async_sessionmaker,
                                    create_async_engine)
from .models import Base


logger = logging.getLogger(__name__)

DB_URL = "postgresql+psycopg://admin:devtoolssecret@172.17.0.1:5433/movies"


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    engine = create_async_engine(DB_URL)
    factory = async_sessionmaker(engine)
    async with factory() as session:
        try:
            yield session
            await session.commit()
        except exc.SQLAlchemyError as error:
            print("sql alchemy error", error)
            await session.rollback()
            raise


async def migrate_tables() -> None:
    logger.info("Start migrating")
    engine = create_async_engine(DB_URL)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    logger.info("Done migrating")


if __name__ == "__main__":
    asyncio.run(migrate_tables())
