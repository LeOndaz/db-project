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
    get_object_or_404,
)


def get_insurance_by_id(db: Session, id) -> models.Insurance:
    return get_db_entity_by_id(db, models.Insurance, id)


def get_insurances(db: Session) -> List[models.Insurance]:
    return get_db_entity_list(db, models.Insurance)


def delete_insurance(db: Session, id) -> models.Insurance:
    return delete_by_entity_by_id(db, models.Insurance, schemas.Insurance, id)


def create_insurance(db: Session, data: schemas.InsuranceCreate) -> models.Insurance:
    return create_db_entity(db, models.Insurance, data)


def update_insurance_by_id(
    db: Session, id: int, data: schemas.InsuranceUpdate
) -> models.Insurance:
    return update_db_entity(db, models.Insurance, id, data)
