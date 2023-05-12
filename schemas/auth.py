from pydantic import BaseModel


class TokenCreate(BaseModel):
    username: str
    password: str
