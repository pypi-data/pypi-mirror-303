from abc import ABC, abstractmethod
import uuid
from datetime import timedelta, datetime
from typing import Union, Optional, List, Protocol

from fastapi import Depends, HTTPException, status
from fastapi.security import APIKeyHeader

from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel


class UserProtocol(Protocol):
    id: uuid.UUID
    user_key: str


class UserCreateProtocol(Protocol):
    user_key: str


class UserFullProtocol(UserProtocol):
    is_superuser: bool
    is_active: bool
    hashed_password: str

    registered_at: datetime
    activated_at: Optional[datetime]
    last_login_at: Optional[datetime]
    accessed_at: Optional[datetime]


class AuthDBBackend(ABC):

    @abstractmethod
    def get_user(self, user_key: str) -> Optional[UserFullProtocol]:
        raise NotImplementedError

    @abstractmethod
    def add_user(self, create: UserCreateProtocol) -> UserFullProtocol:
        raise NotImplementedError

    @abstractmethod
    def access(self, user_key: str) -> None:
        raise NotImplementedError


credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class Auth:

    def __init__(self, db_backend: AuthDBBackend, key_name:str, schema_user, schema_user_full):
        self.auth_scheme = APIKeyHeader(name=key_name)
        self.backend = db_backend
        self.SchemaUser = schema_user
        self.SchemaUserFull = schema_user_full

    def authenticate_user(self, username: str, password: str):
        user = self.backend.get_user(username)
        if not user:
            return False
        return user

    def require_user(self, is_activate: bool = False, is_superuser: bool = False):
        SchemaUserFull = self.SchemaUserFull
        SchemaUser = self.SchemaUser

        def _get_current_user(token: str = Depends(self.auth_scheme)) -> SchemaUserFull:
            user = self.backend.get_user(token)
            if user is None:
                raise credentials_exception
            return SchemaUserFull.model_validate(user)

        def func(user=Depends(_get_current_user)) -> SchemaUser:
            if is_activate and not user.is_active:
                raise credentials_exception

            if is_superuser and not user.is_superuser:
                raise credentials_exception

            return SchemaUser.model_validate(user)

        return func
