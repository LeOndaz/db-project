from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import schemas
from controllers import insurance_controllers
from db import get_db

router = APIRouter(prefix="/insurances", dependencies=[Depends(get_db)])


@router.get("/")
def get_insurances(db: Session = Depends(get_db)) -> List[schemas.Insurance]:
    return insurance_controllers.get_insurances(db)


@router.post("/")
def create_insurance(
    data: schemas.InsuranceCreate, db: Session = Depends(get_db)
) -> schemas.Insurance:
    return insurance_controllers.create_insurance(db, data)


@router.get("/{id}")
def get_insurance_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Insurance:
    return insurance_controllers.get_insurance_by_id(db, id)


@router.put("/{id}")
def update_order_by_id(
    id: int, data: schemas.InsuranceUpdate, db: Session = Depends(get_db)
) -> schemas.Insurance:
    return insurance_controllers.update_insurance_by_id(db, id, data)


@router.delete("/{id}")
def delete_order_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Insurance:
    return insurance_controllers.delete_insurance(db, id)
