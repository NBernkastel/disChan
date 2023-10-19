from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from ..utils import config

Base = declarative_base()

engine = create_async_engine(
    config.DATABASE_URL, future=True
)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def get_async_session():
    async with async_session_maker() as session:
        yield session
