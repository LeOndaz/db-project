from typing import List

from fastapi import Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import product_controllers
from db import get_db

router = APIRouter(prefix="/products", dependencies=[Depends(get_db)])


@router.get("/")
async def get_products(db: Session = Depends(get_db)) -> List[schemas.Product]:
    return product_controllers.get_products(db)


@router.post("/")
@requires(["authenticated"])
async def create_product(
    request: Request, data: schemas.ProductCreate, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.create_product(db, data)


@router.get("/{id}")
async def get_product_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Product:
    return product_controllers.get_product_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
async def update_product_by_id(
    request: Request,
    id: int,
    data: schemas.ProductUpdate,
    db: Session = Depends(get_db),
) -> schemas.Product:
    return product_controllers.update_product_by_id(db, id, data)


@router.get("/{id}/insurances")
async def get_insurances(
    id: int, db: Session = Depends(get_db)
) -> List[schemas.Insurance]:
    return product_controllers.get_insurances(db, id)


@router.post("/{id}/insurances")
@requires(["authenticated"])
async def add_insurance(
    request: Request,
    id: int,
    data: schemas.ProductAddInsurance,
    db: Session = Depends(get_db),
) -> schemas.Product:
    return product_controllers.add_insurance(db, id, data)


@router.delete("/{id}/insurances")
@requires(["authenticated"])
def delete_insurance(
    request: Request,
    id: int,
    data: schemas.ProductRemoveInsurance,
    db: Session = Depends(get_db),
) -> schemas.Product:
    return product_controllers.remove_insurance(db, id, insurance_id=data.insurance_id)


@router.delete("/{id}")
@requires(["authenticated"])
async def delete_product_by_id(
    request: Request, id: int, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.delete_product(db, id)


@router.post("/{id}/sales")
@requires(["authenticated"])
async def add_sale(
    request: Request, id: int, data: schemas.SaleCreate, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.add_sale(db, id, data)


@router.delete("/{id}/sales/{sale_id}")
@requires(["authenticated"])
async def remove_sale(
    request: Request, product_id: int, sale_id: int, db: Session = Depends(get_db)
) -> schemas.Product:
    return product_controllers.remove_sale(db, product_id, sale_id)


@router.get("/{id}/sales")
async def get_sales(id: int, db: Session = Depends(get_db)) -> List[schemas.Sale]:
    return product_controllers.get_sales(db, id)
