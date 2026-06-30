# app/posts/models.py

from app.models.base import BaseTimeStamp
from sqlalchemy.orm import Mapped, mapped_collection
from sqlalchemy import String, BigInteger, Text

class Post(BaseTimeStamp):
    __tablename__ = 'posts'

    id : Mapped[int] =mapped_collection(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )
    title : Mapped[str]=mapped_collection(
        String(255),
        nullable=False
    )
    content : Mapped[str]=mapped_collection(
        Text,
        nullable=False
    )
