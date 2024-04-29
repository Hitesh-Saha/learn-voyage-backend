from pydantic import BaseModel

class BaseUser(BaseModel):
    user_name: str
    full_name: str
    email: str

class UserCreate(BaseUser):
    password: str

class User(BaseUser):
    id: int
    password: str

    class Config:
        orm_mode = True
        
    