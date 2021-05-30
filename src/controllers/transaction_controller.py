from typing import List

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.repositories.postgres.sqlalchemy import get_database
from src.schemas.transaction_schema import TransactionSchema
from src.repositories.postgres.transaction_repository import TransactionRepository

transaction_router = APIRouter(prefix='/transaction')


@transaction_router.get('/', response_model=List[TransactionSchema])
def get_all_transactions(session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transactions = repository.get_all()
    return transactions


# @transaction_router.post('/')
# def create_user(user: UserCreateSchema, session: Session = Depends(get_database)):
#    repository = UserRepository(session)
#    user = repository.create(user)
#    return user


# @transaction_router.delete('/{user_id}')
# def delete_user(user_id: int, session: Session = Depends(get_database)):
#     repository = UserRepository(session)
#     deleted = repository.delete(user_id)
#     if not deleted:
#         message = {'detail': 'User Not Found'}
#         return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=message)
#     else:
#         return f'User {deleted.full_name} successfully deleted.'
