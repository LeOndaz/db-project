from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import schemas
from controllers import customer_controllers
from db import get_db

router = APIRouter(prefix="/customers", dependencies=[Depends(get_db)])


@router.get("/")
def get_customers(db: Session = Depends(get_db)) -> List[schemas.Customer]:
    return customer_controllers.get_customers(db)


@router.post("/")
def create_customer(
    data: schemas.CustomerCreate, db: Session = Depends(get_db)
) -> schemas.Customer:
    return customer_controllers.create_customer(db, data)


@router.get("/{id}")
def get_customer_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Customer:
    return customer_controllers.get_customer_by_id(db, id)


@router.put("/{id}")
def update_customer_by_id(
    id: int, data: schemas.CustomerUpdate, db: Session = Depends(get_db)
) -> schemas.Customer:
    return customer_controllers.update_customer_by_id(db, id, data)


@router.delete("/{id}")
def delete_customer_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Customer:
    return customer_controllers.delete_customer(db, id)
