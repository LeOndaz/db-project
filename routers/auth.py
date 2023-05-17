from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from controllers import auth as auth_controllers
from db import get_db
from schemas.auth import TokenCreate

router = APIRouter(prefix="/auth", dependencies=[Depends(get_db)])


@router.post("/token")
async def token(data: TokenCreate, db: Session = Depends(get_db)):
    return auth_controllers.create_tokens(db, data)
