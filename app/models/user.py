from pydantic import BaseModel
from typing import Optional

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: str
    status: str

    class Config:
        orm_mode = True
