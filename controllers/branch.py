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


def get_branch_by_id(db: Session, id) -> models.Branch:
    return get_db_entity_by_id(db, models.Branch, id)


def get_branches(db: Session) -> List[models.Branch]:
    return get_db_entity_list(db, models.Branch)


def delete_branch(db: Session, id) -> models.Branch:
    return delete_by_entity_by_id(db, models.Branch, schemas.Branch, id)


def create_branch(db: Session, data: schemas.BranchCreate) -> models.Branch:
    return create_db_entity(db, models.Branch, data)


def update_branch_by_id(
    db: Session, id: int, data: schemas.BranchUpdate
) -> models.Branch:
    return update_db_entity(db, models.Branch, id, data)


def get_sales_by_branch_id(db: Session, branch_id: id):
    branch = get_branch_by_id(db, branch_id)
    return branch.sales
