from typing import List

from fastapi import Depends
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session

import schemas
from controllers import branch_controllers
from db import get_db

router = APIRouter(prefix="/branches", dependencies=[Depends(get_db)])


@router.get("/")
def get_branches(db: Session = Depends(get_db)) -> List[schemas.Branch]:
    return branch_controllers.get_branches(db)


@router.post("/")
def create_branch(
    data: schemas.BranchCreate, db: Session = Depends(get_db)
) -> schemas.Branch:
    return branch_controllers.create_branch(db, data)


@router.get("/{id}")
def get_branch_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Branch:
    return branch_controllers.get_branch_by_id(db, id)


@router.put("/{id}")
def update_branch_by_id(
    id: int, data: schemas.BranchUpdate, db: Session = Depends(get_db)
) -> schemas.Branch:
    return branch_controllers.update_branch_by_id(db, id, data)


@router.delete("/{id}")
def delete_branch_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Branch:
    return branch_controllers.delete_branch(db, id)
