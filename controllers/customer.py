from typing import List

from sqlalchemy.orm import Session

import models
import schemas
from utils import (
    create_db_entity,
    delete_by_entity_by_id,
    get_db_entity_by_id,
    get_db_entity_list,
    update_db_entity,
)


def get_customer_by_id(db: Session, id) -> models.Customer:
    return get_db_entity_by_id(db, models.Customer, id)


def get_customers(db: Session) -> List[models.Customer]:
    return get_db_entity_list(db, models.Customer)


def delete_customer(db: Session, id) -> models.Customer:
    return delete_by_entity_by_id(db, models.Customer, schemas.Customer, id)


def create_customer(db: Session, data: schemas.CustomerCreate) -> models.Customer:
    return create_db_entity(db, models.Customer, data)


def update_customer_by_id(
    db: Session, id: int, data: schemas.CustomerUpdate
) -> models.Customer:
    return update_db_entity(db, models.Customer, id, data)
