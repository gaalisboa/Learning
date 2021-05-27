from fastapi import APIRouter

user_router = APIRouter(prefix='/user')


@user_router.get('/')
def get_user_by_id():
    return {'message': 'Hello World'}
