from fastapi import HTTPException, status
from sqlalchemy.orm import Session

import models
from consts import ACCESS_TOKEN_AGE_MINUTES
from models import User
from schemas.auth import TokenCreate
from utils import get_object_or_404
from utils.auth import check_password, create_jwt


def create_tokens(db: Session, data: TokenCreate):
    user: models.User = get_user_by_username(db, data.username)
    valid_pwd = check_password(data.password, user.password)

    if not valid_pwd:
        raise HTTPException(
            detail="Invalid credentials provided", status_code=status.HTTP_403_FORBIDDEN
        )

    jwt = create_jwt(data)

    return {
        "access_token": jwt,
        "available_for": ACCESS_TOKEN_AGE_MINUTES,
        "available_for_unit": "minutes",
    }


def get_user_by_username(db: Session, username):
    return get_object_or_404(db, User, "username", username)
