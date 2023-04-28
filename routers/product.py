from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import schemas
from controllers import product_controllers
from db import get_db

router = APIRouter(prefix="/products", dependencies=[Depends(get_db)])


@router.get("/")
def get_products(db: Session = Depends(get_db)) -> List[schemas.Product]:
    return product_controllers.get_products(db)


@router.post("/")
def create_product(
    data: schemas.ProductCreate, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.create_product(db, data)


@router.get("/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Product:
    return product_controllers.get_product_by_id(db, id)


@router.put("/{id}")
def update_product_by_id(
    id: int, data: schemas.ProductUpdate, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.update_product_by_id(db, id, data)


@router.get("/{id}/insurances")
def get_insurances(id: int, db: Session = Depends(get_db)) -> List[schemas.Insurance]:
    return product_controllers.get_insurances(db, id)


@router.post("/{id}/insurances")
def add_insurance(
    id: int, data: schemas.ProductAddInsurance, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.add_insurance(db, id, data)


@router.delete("/{id}/insurances")
def delete_insurance(
    id: int, data: schemas.ProductRemoveInsurance, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.remove_insurance(db, id, insurance_id=data.insurance_id)


@router.delete("/{id}")
def delete_product_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Product:
    return product_controllers.delete_product(db, id)
