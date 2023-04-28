from typing import Optional

from pydantic import BaseModel, conint

from schemas import Branch


class InsuranceCreate(BaseModel):
    name: str
    discount_percentage: int


class InsuranceUpdate(BaseModel):
    name: Optional[str]
    discount_percentage: Optional[int]


class Insurance(InsuranceCreate):
    id: str

    class Config:
        orm_mode = True


class ProductAddInsurance(BaseModel):
    name: str
    discount_percentage: conint(gt=0)


class ProductRemoveInsurance(BaseModel):
    insurance_id: int
