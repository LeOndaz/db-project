from typing import Optional

from pydantic import BaseModel


class TokenCreate(BaseModel):
    username: str
    password: str


class Me(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    username: str
    email: str
    branch_id: Optional[int]

    class Config:
        orm_mode = True
