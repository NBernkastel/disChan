from typing import Optional

from sqlalchemy import String

from .db_config import Base
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True,nullable=False)
    username: Mapped[str] = mapped_column(String(64),index=True,unique=True,nullable=False)
    email: Mapped[str] = mapped_column(String(120),nullable=False,unique=True)
    hash_pass: Mapped[Optional[str]]= mapped_column(String(128),nullable=False,unique=True)
    salt:Mapped[Optional[str]] = mapped_column(String(1024))
    about_me: Mapped[Optional[str]] = mapped_column(String(140))
