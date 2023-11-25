from repositories.repositories import UserRepository, MessageRepository
from services.message import MessageService
from services.user import UserService


def user_service_fabric():
    return UserService(UserRepository)


def message_service_fabric():
    return MessageService(MessageRepository)
