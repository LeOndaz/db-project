from typing import List

from fastapi import Depends, Request
from fastapi.routing import APIRouter
from sqlalchemy.orm import Session
from starlette.authentication import requires

import schemas
from controllers import branch_controllers
from db import get_db

router = APIRouter(prefix="/branches", dependencies=[Depends(get_db)])


@router.get("/")
async def get_branches(db: Session = Depends(get_db)) -> List[schemas.Branch]:
    return branch_controllers.get_branches(db)


@router.post("/")
@requires(["authenticated"])
async def create_branch(
    request: Request, data: schemas.BranchCreate, db: Session = Depends(get_db)
) -> schemas.Branch:
    return branch_controllers.create_branch(db, data)


@router.get("/{id}")
async def get_branch_by_id(id: int, db: Session = Depends(get_db)) -> schemas.Branch:
    return branch_controllers.get_branch_by_id(db, id)


@router.put("/{id}")
@requires(["authenticated"])
async def update_branch_by_id(
    request: Request, id: int, data: schemas.BranchUpdate, db: Session = Depends(get_db)
) -> schemas.Branch:
    return branch_controllers.update_branch_by_id(db, id, data)


@router.delete("/{id}")
@requires(["authenticated"])
async def delete_branch_by_id(
    request: Request, id: int, db: Session = Depends(get_db)
) -> schemas.Branch:
    return branch_controllers.delete_branch(db, id)


@router.get("/{id}/sales")
async def get_sales(id: int, db: Session = Depends(get_db)) -> List[schemas.Sale]:
    return branch_controllers.get_sales_by_branch_id(db, id)
