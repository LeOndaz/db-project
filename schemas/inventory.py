from typing import Optional

from pydantic import BaseModel, conint

from schemas import Branch


class InventoryCreate(BaseModel):
    name: str
    barcode: str
    branch_id: int


class InventoryUpdate(BaseModel):
    name: Optional[str]
    barcode: Optional[str]
    branch_id: Optional[int]


class Inventory(InventoryCreate):
    id: str
    branch: Branch

    class Config:
        orm_mode = True


class RemoveProductFromInventory(BaseModel):
    product_id: int


class AddProductToInventory(RemoveProductFromInventory):
    product_id: int
    quantity: conint(gt=0)
