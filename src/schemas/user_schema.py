from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    full_name: str
    email: str
    phone_number: str
    created_at: str
    updated_at: str
