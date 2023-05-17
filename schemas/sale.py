from datetime import datetime
from typing import Optional
from decimal import Decimal

from pydantic import BaseModel, condecimal, conint, root_validator


class SaleCreate(BaseModel):
    starts_at: datetime
    ends_at: datetime
    amount: Optional[condecimal(gt=Decimal(0))]
    percentage: Optional[condecimal(gt=Decimal(0), le=Decimal(0), decimal_places=2)]
    branch_id: Optional[conint(gt=0)]

    starts_at: datetime
    ends_at: datetime

    @root_validator()
    def validate_starts_in_future(cls, values):
        starts_at = values['starts_at']
        ends_at = values['ends_at']

        if not starts_at < ends_at:
            raise ValueError("starts_at must be before ends_at")

        return values

    @root_validator()
    def validate_on_of_amount_or_percentage(cls, values):
        amount = values.get('amount')
        percentage = values.get('percentage')

        if amount and percentage:
            raise ValueError("amount and percentage are mutually exclusive. Please only provide one of them")

        if not amount and not percentage:
            raise ValueError('amount or percentage are not provided')

        return values


class Sale(SaleCreate):
    id: int
