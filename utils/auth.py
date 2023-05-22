from datetime import datetime, timedelta

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

import models
from consts import (
    ACCESS_TOKEN_AGE_MINUTES,
    ADMIN_PASSWORD,
    ADMIN_USERNAME,
    JWT_ALGORITHM,
    SECRET_KEY,
)
from db import get_db
from schemas.auth import TokenCreate

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def check_password(pwd, hashed_pwd):
    return pwd_context.verify(pwd, hashed_pwd)


def hash_password(password):
    return pwd_context.hash(password)


def authenticate(db: Session, identifier_value, password, identifier_field="email"):
    assert identifier_field in (
        "email",
        "username",
    ), "user is identified by email/username only"

    user = db.get(models.User, {identifier_field: identifier_value})

    if user and check_password(password, user.password):
        return user

    return None


def create_jwt(user: TokenCreate, duration=timedelta(minutes=ACCESS_TOKEN_AGE_MINUTES)):
    expires_at = datetime.utcnow() + duration

    return jwt.encode(
        {
            "exp": expires_at,
            "username": user.username,
        },
        SECRET_KEY,
        JWT_ALGORITHM,
    )


def decode_jwt(token):
    return jwt.decode(token, SECRET_KEY, JWT_ALGORITHM)


def init_admin(branch_id):
    db = next(get_db())
    user = models.User(
        username=ADMIN_USERNAME,
        email="admin@admin.com",
        is_staff=True,
        branch_id=branch_id
    )
    user.password = hash_password(ADMIN_PASSWORD)
    db.add(user)
    db.commit()
