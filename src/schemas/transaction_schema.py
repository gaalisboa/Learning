from datetime import datetime

from pydantic import BaseModel


class TransactionSchema(BaseModel):
    id: int
    user_id: int
    description: str
    category: str
    cost: float
    date: datetime


class TransactionCreateSchema(BaseModel):
    user_id: int
    description: str
    category: str
    cost: float
