from typing import Optional

from pydantic import BaseModel, validator

from utils import validate_phone_number


class BranchCreate(BaseModel):
    name: str
    address: str
    phone_number: str

    validate_phone_number = validator("phone_number", allow_reuse=True)(
        validate_phone_number
    )


class BranchUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]


class Branch(BranchCreate):
    id: int

    class Config:
        orm_mode = True
