from datetime import date
from decimal import Decimal
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, condecimal, validator

from utils.enums import ProductType

from .sale import Sale


class ProductTypeDisplay(str, Enum):
    DRUG = "DRUG"
    BEAUTY = "BEAUTY"


class ProductCreate(BaseModel):
    name: str
    price: condecimal(gt=Decimal(0))
    expiration_date: date
    barcode: str
    type: Optional[ProductTypeDisplay]

    @validator("type")
    def validate_product_type(cls, value):
        return ProductType[value]


class ProductUpdate(BaseModel):
    name: Optional[str]
    price: Optional[condecimal(gt=Decimal(0))]
    expiration_date: Optional[date]
    barcode: Optional[str]
    type: Optional[str]


class Product(ProductCreate):
    id: str
    type: ProductTypeDisplay
    sales: List[Sale]

    @validator("type", pre=True)
    def validate_product_type(cls, value):
        for member_name, member_value in ProductTypeDisplay.__members__.items():
            if value == member_value:
                return member_name

    class Config:
        orm_mode = True
