import typing

from fastapi.exceptions import HTTPException
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    UnauthenticatedUser,
)
from starlette.requests import HTTPConnection

import models
from controllers.auth import get_user_by_username
from db import get_db
from utils.auth import decode_jwt


class JWTBackend(AuthenticationBackend):
    async def authenticate(
        self, conn: HTTPConnection
    ) -> typing.Optional[
        typing.Tuple["AuthCredentials", typing.Union[models.User, UnauthenticatedUser]]
    ]:
        scopes = []
        authorization = conn.headers.get("Authorization")

        if not authorization:
            return AuthCredentials(scopes), UnauthenticatedUser()

        _, token = authorization.split()
        payload = decode_jwt(token)

        username = payload.get("username")

        if username is None:
            raise HTTPException(detail="Invalid JWT token", status_code=401)

        db = next(get_db())
        user = get_user_by_username(db, username)

        if user:
            scopes.append("authenticated")

        return AuthCredentials(scopes), user
