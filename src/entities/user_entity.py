from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from src.repositories.postgres.sqlalchemy import Base


class UserEntity(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(255), index=True)
    email = Column(String(100))
    phone_number = Column(String(16))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, default=datetime.now(), onupdate=datetime.now())

    transactions = relationship("TransactionEntity", back_populates="owner")
