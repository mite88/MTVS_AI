# app/models/base.py

# ORM
from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_collection
from datetime import datetime

class BaseTimeStamp(DeclarativeBase):

    __abstract__ = True # 추상으로 함(안하면 테이블로 인식해서 만들어버림)

    created_at : Mapped[datetime] = mapped_collection(
        DateTime, #sql문법에서의 datetime
        default=datetime.now(),
        nullable=False
    )

    updated_at: Mapped[datetime] = mapped_collection(
        DateTime,  # sql문법에서의 datetime
        default=datetime.now(),
        nullable=False
    )