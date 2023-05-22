import typing

from fastapi.exceptions import HTTPException
from starlette.authentication import (
    AuthCredentials,
    AuthenticationBackend,
    AuthenticationError,
    UnauthenticatedUser,
)
from starlette.requests import HTTPConnection

import models
from controllers.auth import get_user_by_username
from db import get_db
from utils.auth import decode_jwt
from jose import JWTError


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

        bearer, token = authorization.split()

        if bearer != "Bearer":
            raise AuthenticationError("Invalid authorization header")

        try:
            payload = decode_jwt(token)
        except JWTError:
            raise AuthenticationError("invalid token passed")

        username = payload.get("username")

        if username is None:
            raise AuthenticationError("Invalid JWT token")

        db = next(get_db())
        user = get_user_by_username(db, username)

        if user:
            scopes.append("authenticated")

        return AuthCredentials(scopes), user
