from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import schemas
from controllers import order_controllers
from db import get_db

router = APIRouter(prefix="/orders", dependencies=[Depends(get_db)])


@router.get("/")
def get_orders(db: Session = Depends(get_db)) -> List[schemas.Order]:
    return order_controllers.get_orders(db)


@router.post("/")
def create_order(
    data: schemas.OrderCreate, db: Session = Depends(get_db)
) -> schemas.Order:
    return order_controllers.create_order(db, data)


@router.get("/{id}")
def get_order_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Order:
    return order_controllers.get_order_by_id(db, id)


@router.put("/{id}")
def update_order_by_id(
    id: int, data: schemas.OrderUpdate, db: Session = Depends(get_db)
) -> schemas.Order:
    return order_controllers.update_order_by_id(db, id, data)


@router.delete("/{id}")
def delete_order_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Order:
    return order_controllers.delete_order(db, id)
