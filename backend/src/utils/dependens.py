from repositories.repositories import UserRepository, MessageRepository, UserToUserRepository
from services.message import MessageService
from services.user import UserService


def user_service_fabric():
    return UserService(UserRepository)

def user_to_user_fabric():
    return UserService(UserToUserRepository)


def message_service_fabric():
    return MessageService(MessageRepository)
