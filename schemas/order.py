from datetime import datetime
from decimal import Decimal
from typing import List, Optional, Union

from pydantic import BaseModel, condecimal

from .branch import Branch
from .customer import Customer
from .product import Product


class OrderLine(BaseModel):
    product: "Product"
    quantity: int
    order_id: int

    class Config:
        orm_mode = True


class OrderLineCreate(BaseModel):
    product_id: int
    quantity: int
    insurance_id: Optional[int]


class OrderCreate(BaseModel):
    branch_id: int
    customer_id: int
    lines: List[OrderLineCreate]


class OrderUpdate(BaseModel):
    pass


class Order(BaseModel):
    id: str
    price: Decimal
    amount_paid: Union[Decimal, None]
    created_at: datetime

    branch: Branch
    customer: Customer
    lines: List[OrderLine]

    class Config:
        orm_mode = True
