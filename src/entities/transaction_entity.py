from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.sql.schema import ForeignKey

from src.repositories.postgres.sqlalchemy import Base


class TransactionEntity(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer)
    description = Column(String(255))
    category = Column(String(255))
    cost = Column(Float)
    date = Column(DateTime, default=datetime.now())
