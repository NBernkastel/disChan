from abc import ABC, abstractmethod
from ..database.db_config import async_session_maker


class AbstractRepository(ABC):
    pass


class SQLAlchemyRepository(AbstractRepository):
    model = None
