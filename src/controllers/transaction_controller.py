from typing import List

from sqlalchemy.orm import Session

from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.repositories.postgres.sqlalchemy import get_database
from src.schemas.transaction_schema import TransactionCreateSchema, TransactionSchema
from src.repositories.postgres.transaction_repository import TransactionRepository

transaction_router = APIRouter(prefix='/transaction')


@transaction_router.get('/', response_model=List[TransactionSchema])
def get_all_transactions(session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transactions = repository.get_all()
    return transactions


@transaction_router.get('/{user_id}', response_model=List[TransactionSchema])
def get_transactions_by_user_id(user_id: int, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transactions = repository.get_by_user_id(user_id)
    return transactions


@transaction_router.post('/')
def create_transaction(transaction: TransactionCreateSchema, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.create(transaction)
    return transaction


@transaction_router.get('/{transaction_id}', response_model=List[TransactionSchema])
def get_transaction_by_id(transaction_id: int, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.get_one(transaction_id)
    if not transaction:
        message = {'detail': 'Transaction Not Found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=message)
    else:
        return transaction


@transaction_router.put('/{transaction_id}', response_model=List[TransactionSchema])
def update_transaction(transaction_id: int, transaction: TransactionCreateSchema,
                       session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    transaction = repository.update(transaction_id, transaction)
    if not transaction:
        message = {'detail': 'Transaction Not Found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=message)
    else:
        return transaction


@transaction_router.delete('/{transaction_id}')
def delete_transaction(transaction_id: int, session: Session = Depends(get_database)):
    repository = TransactionRepository(session)
    deleted = repository.delete(transaction_id)
    if not deleted:
        message = {'detail': 'Transaction Not Found'}
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=message)
    else:
        return 'Transaction successfully deleted.'
