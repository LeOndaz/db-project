from typing import List

from fastapi import Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import inventory_controllers
from db import get_db

router = APIRouter(prefix="/inventories", dependencies=[Depends(get_db)])


@router.get("/")
def get_inventories(db: Session = Depends(get_db)) -> List[schemas.Inventory]:
    return inventory_controllers.get_inventories(db)


@router.post("/")
@requires(["authenticated"])
def create_inventory(
    request: Request, data: schemas.InventoryCreate, db: Session = Depends(get_db)
) -> schemas.Inventory:
    return inventory_controllers.create_inventory(db, data)


@router.get("/{id}")
def get_inventory_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Inventory:
    return inventory_controllers.get_inventory_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
def update_inventory_by_id(
    request: Request,
    id: int,
    data: schemas.InventoryUpdate,
    db: Session = Depends(get_db),
) -> schemas.Inventory:
    return inventory_controllers.update_inventory_by_id(db, id, data)


@router.delete("/{id}")
@requires(["authenticated"])
def delete_inventory_by_id(
    request: Request, id: int, db: Session = Depends(get_db)
) -> schemas.Inventory:
    return inventory_controllers.delete_inventory(db, id)


@router.put("/{id}/remove-product")
@requires(["authenticated"])
def remove_product_from_inventory(
    request: Request,
    id: int,
    data: schemas.RemoveProductFromInventory,
    db: Session = Depends(get_db),
) -> schemas.Inventory:
    return inventory_controllers.remove_product_from_inventory(db, id, data.product_id)


@router.put("/{id}/add-product")
@requires(["authenticated"])
def add_product_to_inventory(
    request: Request,
    id: int,
    data: schemas.AddProductToInventory,
    db: Session = Depends(get_db),
) -> schemas.Inventory:
    return inventory_controllers.add_product_to_inventory(db, id, data)
