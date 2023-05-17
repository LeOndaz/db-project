from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from schemas.sale import SaleCreate
from utils import (
    create_db_entity,
    delete_by_entity_by_id,
    get_db_entity_by_id,
    get_db_entity_list,
    get_object_or_404,
    update_db_entity,
)


def get_product_by_id(db: Session, id) -> models.Product:
    return get_db_entity_by_id(db, models.Product, id)


def get_products(db: Session) -> List[models.Product]:
    return get_db_entity_list(db, models.Product)


def delete_product(db: Session, id) -> models.Product:
    return delete_by_entity_by_id(db, models.Product, schemas.Product, id)


def create_product(db: Session, data: schemas.ProductCreate) -> models.Product:
    return create_db_entity(db, models.Product, data)


def update_product_by_id(
    db: Session, id: int, data: schemas.ProductUpdate
) -> models.Product:
    return update_db_entity(db, models.Product, id, data)


def add_insurance(
    db: Session, product_id: int, data: schemas.ProductAddInsurance
) -> models.Product:
    # product first, to avoid creating insurance and then throwing error bloating the db
    product = get_object_or_404(db, models.Product, "id", product_id)

    insurance = models.Insurance(
        name=data.name,
        discount_percentage=data.discount_percentage,
    )
    db.add(insurance)
    db.commit()

    product_insurance = models.ProductInsurance(
        product=product,
        insurance=insurance,
    )
    db.add(product_insurance)
    db.commit()

    db.refresh(product)

    return product


def get_insurances(db: Session, product_id: int):
    product = get_object_or_404(db, models.Product, "id", product_id)
    product_insurances = product.product_insurances

    def mapper(product_insurance):
        return product_insurance.insurance

    return list(map(mapper, product_insurances))


def remove_insurance(db: Session, product_id: int, insurance_id: int) -> models.Product:
    product: models.Product = get_object_or_404(db, models.Product, "id", product_id)

    for product_insurance in product.product_insurances:
        if product_insurance.insurance == insurance_id:
            product.product_insurances.remove(product_insurance)
            db.commit()
            break

    db.refresh(product)
    return product


def add_sale(db: Session, product_id: int, data: SaleCreate):
    assert (
        data.percentage or data.amount
    ), "Must either provide a percentage or an amount"

    product: models.Product = get_object_or_404(db, models.Product, "id", product_id)

    if data.branch_id:
        branch = get_object_or_404(db, models.Branch, "id", data.branch_id)
    else:
        branch = None

    sale = models.Sale(
        branch=branch,
        amount=data.amount,
        percentage=data.percentage,
        product=product,
        starts_at=data.starts_at,
        ends_at=data.ends_at,
    )
    db.add(sale)
    db.commit()

    return product


def remove_sale(db: Session, product_id: int, sale_id: int):
    product = get_object_or_404(db, models.Product, "id", product_id)
    delete_by_entity_by_id(db, models.Sale, schemas.Sale, sale_id)
    return product


def get_sales(db: Session, product_id: int):
    product: models.Product = get_object_or_404(db, models.Product, "id", product_id)
    return product.sales
