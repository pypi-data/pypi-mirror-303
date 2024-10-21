import logging
from datetime import timedelta

from fastapi import HTTPException as BaseHTTPException
from fastapi.openapi.models import HTTPBearer, SecuritySchemeType
from fastapi.security.base import SecurityBase
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, JWTError
from jose.constants import ALGORITHMS
from pydantic import ValidationError
from starlette import status
from starlette.authentication import AuthenticationError
from starlette.requests import HTTPConnection
from starlette.responses import Response
from tortoise.timezone import now

from x_auth.enums import FailReason, AuthFailReason
from x_auth.pydantic import AuthUser

cookie_name = "access_token"


class HTTPException(BaseHTTPException):
    def __init__(
        self,
        reason: FailReason | AuthFailReason,
        parent: Exception | str = None,
        status_: status = status.HTTP_400_BAD_REQUEST,
        hdrs: dict = None,
    ) -> None:
        detail = f"{reason.name}{f': {parent}' if parent else ''}"
        logging.error(detail)
        super().__init__(status_, detail, hdrs)


class AuthException(HTTPException, AuthenticationError):
    def __init__(
        self,
        reason: AuthFailReason,
        parent: Exception | str = None,
        status_: status = status.HTTP_401_UNAUTHORIZED,
        cookie_name_: str | None = cookie_name,
    ) -> None:
        # todo add: path=/; domain=; secure; ...
        hdrs = {"set-cookie": cookie_name_ + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT"} if cookie_name_ else None
        super().__init__(reason=reason, parent=parent, status_=status_, hdrs=hdrs)


class BearerBase(SecurityBase):
    """HTTP Bearer token authentication"""

    scheme_name = "bearer"

    def __init__(self, auto_error: bool = True, type_: SecuritySchemeType = SecuritySchemeType.http):
        self.model = HTTPBearer(type=type_)
        self.auto_error = auto_error

    async def __call__(self, conn: HTTPConnection) -> str | None:
        authorization = conn.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            if self.auto_error:
                raise AuthException(reason=AuthFailReason.header, parent="Not authenticated")
            else:
                return None
        if scheme.lower() != "bearer":
            if self.auto_error:
                raise AuthException(reason=AuthFailReason.scheme, parent="Not Bearer scheme")
            else:
                return None
        return credentials


def on_error(_: HTTPConnection, exc: AuthException) -> Response:
    hdr = {}
    if exc.status_code == 303 and "/login" in (r.path for r in _.app.routes):
        hdr = {"Location": "/login"}
    resp = Response(str(exc), status_code=exc.status_code, headers=hdr)
    resp.delete_cookie(cookie_name)
    return resp


def jwt_encode(data: AuthUser, secret: str, expires_delta: timedelta) -> str:
    return jwt.encode({"exp": now() + expires_delta, **data.model_dump()}, secret, ALGORITHMS.HS256)


def jwt_decode(jwtoken: str, secret: str, verify_exp: bool = True) -> AuthUser:
    try:
        payload = jwt.decode(jwtoken, secret, ALGORITHMS.HS256, {"verify_exp": verify_exp})
        return AuthUser(**payload)
    except (ValidationError, JWTError) as e:
        raise AuthException(AuthFailReason.signature, parent=e)
