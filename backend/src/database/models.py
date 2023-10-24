from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from .db_config import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(64), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False, unique=True)
    hash_pass: Mapped[str] = mapped_column(String(128), nullable=False)
    salt: Mapped[str] = mapped_column(String(32), nullable=False)
    about_me: Mapped[str] = mapped_column(String(140), nullable=True)


class UserToUser(Base):
    __tablename__ = 'user_to_user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_user: Mapped[int] = mapped_column(ForeignKey('user.id'))
    second_user: Mapped[int] = mapped_column(ForeignKey('user.id'))
    is_friend: Mapped[bool] = mapped_column(default=False)


class Role(Base):
    __tablename__ = 'role'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    server = mapped_column(ForeignKey('server.id'))
    is_admin: Mapped[bool] = mapped_column(default=False)
    can_mute: Mapped[bool] = mapped_column(default=False)
    can_kick: Mapped[bool] = mapped_column(default=False)
    can_ban: Mapped[bool] = mapped_column(default=False)
    can_edit: Mapped[bool] = mapped_column(default=False)


class Server(Base):
    __tablename__ = 'server'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    language: Mapped[str] = mapped_column(String(3), nullable=False)


class Channel(Base):
    __tablename__ = 'channel'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    channel_name: Mapped[str] = mapped_column(String(32), nullable=False)
    text_or_voice: Mapped[bool] = mapped_column(default=False)


class UserServerRole(Base):
    __tablename__ = 'user_server_role'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user = mapped_column(ForeignKey('user.id'))
    server = mapped_column(ForeignKey('server.id'))
    role = mapped_column(ForeignKey('role.id'))


class ServerChannelRole(Base):
    __tablename__ = 'server_channel_role'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    server = mapped_column(ForeignKey('server.id'))
    channel = mapped_column(ForeignKey('channel.id'))
    role = mapped_column(ForeignKey('role.id'))


class Message(Base):
    __tablename__ = 'message'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_from = mapped_column(ForeignKey('user.id'))
    channel = mapped_column(ForeignKey('channel.id'))
    server = mapped_column(ForeignKey('server.id'), nullable=True)
    body: Mapped[str]
    is_delete: Mapped[bool] = mapped_column(default=False)
