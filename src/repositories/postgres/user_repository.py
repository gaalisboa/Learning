from sqlalchemy.orm import Session

from src.schemas.user_schema import UserSchema, UserCreateSchema
from src.entities.user_entity import UserEntity


class UserRepository:

    def __init__(self, database_session: Session):
        self.__database = database_session

    def is_connected(self) -> bool:
        return True if self.__database else False

    def get_all(self):
        db_users = self.__database.query(UserEntity).all()
        users = [UserSchema(**user.__dict__) for user in db_users]
        return users

    def get_one(self, user_id):
        db_user = self.__database.query(UserEntity).get(user_id)

        if not db_user:
            return None

        else:
            user = UserSchema(**db_user.__dict__)
            return user

    def create(self, user: UserCreateSchema):
        db_user = UserEntity(**user.__dict__)

        self.__database.add(db_user)
        self.__database.commit()
        self.__database.refresh(db_user)

        user_schema = UserSchema(**db_user.__dict__)
        return user_schema

    def update(self, user_id, user: UserCreateSchema):
        db_user = self.__database.query(UserEntity).get(user_id)

        if not db_user:
            return None

        updated_user = user.__dict__

        for key, value in updated_user.items():
            setattr(db_user, key, value)

        self.__database.commit()
        self.__database.refresh(db_user)
        user_schema = UserSchema(**db_user.__dict__)
        return user_schema

    def delete(self, user_id):
        user = self.__database.query(UserEntity).get(user_id)

        if not user:
            return None

        self.__database.delete(user)
        self.__database.commit()

        return user
