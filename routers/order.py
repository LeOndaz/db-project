from typing import Annotated, List, Union

from fastapi import Body, Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import order_controllers
from db import get_db

router = APIRouter(prefix="/orders", dependencies=[Depends(get_db)])


@router.get("/")
async def get_orders(
    branch_id: Union[int, None] = None, db: Session = Depends(get_db)
) -> List[schemas.Order]:
    return order_controllers.get_orders(db, branch_id)


@router.post("/")
@requires(["authenticated"])
async def create_order(
    request: Request, data: schemas.OrderCreate, db: Session = Depends(get_db)
) -> schemas.Order:
    return order_controllers.create_order(db, data)


@router.get("/{id}")
async def get_order_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Order:
    return order_controllers.get_order_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
async def update_order_by_id(
    request: Request, id: int, data: schemas.OrderUpdate, db: Session = Depends(get_db)
) -> schemas.Order:
    return order_controllers.update_order_by_id(db, id, data)


@router.delete("/{id}")
@requires(["authenticated"])
async def delete_order_by_id(
    request: Request, id: int, db: Session = Depends(get_db)
) -> schemas.Order:
    return order_controllers.delete_order(db, id)
