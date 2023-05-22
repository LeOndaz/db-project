from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from utils import (
    create_db_entity,
    delete_by_entity_by_id,
    get_db_entity_by_id,
    get_db_entity_list,
    update_db_entity, get_object_or_404,
)


def get_customer_by_id(db: Session, id) -> models.Customer:
    return get_db_entity_by_id(db, models.Customer, id)


def get_customers(db: Session, limit: int, offset: int) -> List[models.Customer]:
    return get_db_entity_list(db, models.Customer, limit, offset)


def delete_customer(db: Session, id) -> models.Customer:
    return delete_by_entity_by_id(db, models.Customer, schemas.Customer, id)


def create_customer(db: Session, data: schemas.CustomerCreate) -> models.Customer:
    return create_db_entity(db, models.Customer, data)


def update_customer_by_id(
        db: Session, id: int, data: schemas.CustomerUpdate
) -> models.Customer:
    return update_db_entity(db, models.Customer, id, data)


def add_insurance(
        db: Session, customer_id: int, data: schemas.CustomerAddInsurance
) -> models.Customer:
    # product first, to avoid creating insurance and then throwing error bloating the db
    customer = get_object_or_404(db, models.Customer, "id", customer_id)

    insurance = models.Insurance(
        name=data.name,
        discount_percentage=data.discount_percentage,
    )
    db.add(insurance)
    db.commit()

    customer_insurance = models.ProductInsurance(
        customer=customer,
        insurance=insurance,
    )
    db.add(customer_insurance)
    db.commit()
    return customer


def get_insurances(db: Session, customer_id: int):
    customer = get_object_or_404(db, models.Customer, "id", customer_id)
    customer_insurances = customer.customer_insurances

    def mapper(customer_insurance):
        return customer_insurance.insurance

    return list(map(mapper, customer_insurances))


def remove_insurance(db: Session, customer_id: int, insurance_id: int) -> models.Customer:
    customer: models.Customer = get_object_or_404(db, models.Customer, "id", customer_id)

    for customer_insurance in customer.customer_insurances:
        if customer_insurance.insurance == insurance_id:
            customer.customer_insurances.remove(customer_insurance)
            db.commit()
            break

    return customer
