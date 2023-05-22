from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from starlette.authentication import requires

from controllers import auth as auth_controllers
from db import get_db
from schemas.auth import TokenCreate, Me

router = APIRouter(prefix="/auth", dependencies=[Depends(get_db)])


@router.post("/token")
async def token(data: TokenCreate, db: Session = Depends(get_db)):
    return auth_controllers.create_tokens(db, data)


@router.get("/me")
@requires(["authenticated"])
async def me(request: Request):
    return Me.from_orm(request.user)
