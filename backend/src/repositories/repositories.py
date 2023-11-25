from utils.repository import SQLAlchemyRepository
from database.models import User, Message


class UserRepository(SQLAlchemyRepository):
    model = User


class MessageRepository(SQLAlchemyRepository):
    model = Message
