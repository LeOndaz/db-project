from typing import List

from fastapi import Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import customer_controllers
from db import get_db

router = APIRouter(prefix="/customers", dependencies=[Depends(get_db)])


@router.get("/")
async def get_customers(db: Session = Depends(get_db), limit: int = 100, offset: int = 0) -> List[schemas.Customer]:
    return customer_controllers.get_customers(db, limit, offset)


@router.post("/")
@requires(["authenticated"])
async def create_customer(
        request: Request, data: schemas.CustomerCreate, db: Session = Depends(get_db)
) -> schemas.Customer:
    return customer_controllers.create_customer(db, data)


@router.get("/{id}")
def get_customer_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Customer:
    return customer_controllers.get_customer_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
async def update_customer_by_id(
        request: Request,
        id: int,
        data: schemas.CustomerUpdate,
        db: Session = Depends(get_db),
) -> schemas.Customer:
    return customer_controllers.update_customer_by_id(db, id, data)


@router.delete("/{id}")
@requires(["authenticated"])
async def delete_customer_by_id(
        request: Request, id: int, db: Session = Depends(get_db)
) -> schemas.Customer:
    return customer_controllers.delete_customer(db, id)


@router.get("/{id}/insurances")
async def get_insurances(
    id: int, db: Session = Depends(get_db)
) -> List[schemas.Insurance]:
    return customer_controllers.get_insurances(db, id)


@router.post("/{id}/insurances")
@requires(["authenticated"])
async def add_insurance(
    request: Request,
    id: int,
    data: schemas.CustomerAddInsurance,
    db: Session = Depends(get_db),
) -> schemas.Customer:
    return customer_controllers.add_insurance(db, id, data)


@router.delete("/{id}/insurances")
@requires(["authenticated"])
def delete_insurance(
    request: Request,
    id: int,
    data: schemas.CustomerRemoveInsurance,
    db: Session = Depends(get_db),
) -> schemas.Customer:
    return customer_controllers.remove_insurance(db, id, insurance_id=data.insurance_id)
