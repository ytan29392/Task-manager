from pydantic import BaseModel, EmailStr
from typing import Optional

# --------------------------
# Request schema for registration / login
# --------------------------
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# --------------------------
# Response schema (exclude password)
# --------------------------
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True

# --------------------------
# Token schema (JWT)
# --------------------------
class Token(BaseModel):
    access_token: str
    token_type: str
