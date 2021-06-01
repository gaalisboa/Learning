from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from src.repositories.postgres.sqlalchemy import Base


class TransactionEntity(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String(255))
    category = Column(String(255))
    cost = Column(Float)
    date = Column(DateTime, default=datetime.now())

    owner = relationship("UserEntity", back_populates="transactions")
