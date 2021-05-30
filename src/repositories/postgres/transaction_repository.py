from sqlalchemy.orm import Session

from src.schemas.transaction_schema import TransactionCreateSchema, TransactionSchema
from src.entities.transaction_entity import TransactionEntity


class TransactionRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        db_transactions = self.__database.query(TransactionEntity).all()
        transactions = [TransactionSchema(**transaction.__dict__) for transaction in db_transactions]
        return transactions

    def get_one(self, transaction_id):
        db_transaction = self.__database.query(TransactionEntity).get(transaction_id)

        if not db_transaction:
            return None

        else:
            transaction = TransactionSchema(**db_transaction.__dict__)
            return transaction

    def create(self, transaction: TransactionCreateSchema):
        db_transaction = TransactionEntity(**transaction.__dict__)

        self.__database.add(db_transaction)
        self.__database.commit()
        self.__database.refresh(db_transaction)

        transaction_schema = TransactionSchema(**db_transaction.__dict__)
        return transaction_schema

    def update(self, transaction_id, transaction: TransactionCreateSchema):
        db_transaction = self.__database.query(TransactionEntity).get(transaction_id)

        if not db_transaction:
            return None

        updated_transaction = transaction.__dict__

        for key, value in updated_transaction.items():
            setattr(db_transaction, key, value)

        self.__database.commit()
        self.__database.refresh(db_transaction)
        transaction_schema = TransactionSchema(**db_transaction.__dict__)
        return transaction_schema

    def delete(self, transaction_id):
        transaction = self.__database.query(TransactionEntity).get(transaction_id)

        if not transaction:
            return None

        self.__database.delete(transaction)
        self.__database.commit()

        return transaction
