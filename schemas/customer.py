from typing import Optional

from pydantic import BaseModel, validator

from utils import validate_phone_number


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str

    validate_phone_number = validator("phone_number", allow_reuse=True)(
        validate_phone_number
    )


class CustomerUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]

    validate_phone_number = validator("phone_number", allow_reuse=True)(
        validate_phone_number
    )


class Customer(CustomerCreate):
    id: str
    first_name: str
    last_name: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True
