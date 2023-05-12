from typing import List

from fastapi import Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import insurance_controllers
from db import get_db

router = APIRouter(prefix="/insurances", dependencies=[Depends(get_db)])


@router.get("/")
def get_insurances(db: Session = Depends(get_db)) -> List[schemas.Insurance]:
    return insurance_controllers.get_insurances(db)


@router.post("/")
@requires(["authenticated"])
def create_insurance(
    request: Request, data: schemas.InsuranceCreate, db: Session = Depends(get_db)
) -> schemas.Insurance:
    return insurance_controllers.create_insurance(db, data)


@router.get("/{id}")
def get_insurance_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Insurance:
    return insurance_controllers.get_insurance_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
def update_order_by_id(
    request: Request, id: int, data: schemas.InsuranceUpdate, db: Session = Depends(get_db)
) -> schemas.Insurance:
    return insurance_controllers.update_insurance_by_id(db, id, data)


@router.delete("/{id}")
@requires(["authenticated"])
def delete_order_by_id(request: Request, id: int, db: Session = Depends(get_db)) -> schemas.Insurance:
    return insurance_controllers.delete_insurance(db, id)
