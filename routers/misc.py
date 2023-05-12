from fastapi import APIRouter, BackgroundTasks, Depends, Request
from sqlalchemy.orm import Session
from starlette.authentication import requires

from db import get_db
from utils import create_tables, drop_tables
from utils.fixtures import setup_db_data

router = APIRouter(prefix="/misc", dependencies=[Depends(get_db)])


@router.post("/refill-db")
@requires(["authenticated"])
def refill_db(
    request: Request, background_tasks: BackgroundTasks, db: Session = Depends(get_db)
):
    drop_tables(db)
    create_tables(db)
    background_tasks.add_task(setup_db_data)
    return {"done": True}
