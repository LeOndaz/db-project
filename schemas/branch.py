from typing import Optional

from pydantic import BaseModel


class BranchCreate(BaseModel):
    name: str
    address: str
    phone_number: str


class BranchUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class Branch(BranchCreate):
    id: str

    class Config:
        orm_mode = True
