from typing import Optional

from pydantic import BaseModel


class CustomerCreate(BaseModel):
    first_name: str
    last_name: str
    phone_number: str
    address: str


class CustomerUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    phone_number: Optional[str]
    address: Optional[str]


class Customer(CustomerCreate):
    id: str
    first_name: str
    last_name: str
    phone_number: str
    address: str

    class Config:
        orm_mode = True
