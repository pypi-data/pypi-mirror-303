from abc import ABC, abstractmethod
import uuid
from datetime import timedelta, datetime
from typing import Union, Optional, List, Protocol

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, SecurityScopes

from jose import jwt, JWTError
from passlib.context import CryptContext
from pydantic import BaseModel


class UserProtocol(Protocol):
    id: uuid.UUID
    username: str
    scopes: Optional[str]


class UserCreateProtocol(Protocol):
    username: str
    password: str


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
    async def get_user(self, username: str) -> Optional[UserFullProtocol]:
        raise NotImplementedError

    @abstractmethod
    async def add_user(self, create: UserCreateProtocol, hashed_password: str) -> UserFullProtocol:
        raise NotImplementedError

    @abstractmethod
    async def access(self, username: str) -> None:
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

    def __init__(self, secret_key, algorithm, access_token_expire_minutes, db_backend: AuthDBBackend,
                 schema_user, schema_user_full):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
        self.SECRET_KEY, self.ALGORITHM = secret_key, algorithm
        self.ACCESS_TOKEN_EXPIRE_MINUTES = access_token_expire_minutes
        self.backend = db_backend
        self.SchemaUser = schema_user
        self.SchemaUserFull = schema_user_full

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def create_access_token(self, data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=self.ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.SECRET_KEY, algorithm=self.ALGORITHM)
        return encoded_jwt

    async def authenticate_user(self, username: str, password: str):
        user = await self.backend.get_user(username)
        if not user:
            return False
        if not self.verify_password(password, user.hashed_password):
            return False
        return user

    def require_user(self, is_activate: bool = False, is_superuser: bool = False):
        SchemaUserFull = self.SchemaUserFull
        SchemaUser = self.SchemaUser

        async def _get_current_user(token: str = Depends(self.oauth2_scheme)) -> SchemaUserFull:
            try:
                payload = jwt.decode(token, self.SECRET_KEY, algorithms=[self.ALGORITHM])
                username: str = payload.get("sub")
                if username is None:
                    raise credentials_exception
                token_data = TokenData(username=username)
            except JWTError:
                raise credentials_exception
            user = await self.backend.get_user(token_data.username)
            await self.backend.access(token_data.username)
            return SchemaUserFull.model_validate(user)

        async def func(security_scopes: SecurityScopes, user=Depends(_get_current_user)) -> SchemaUser:
            if is_activate and not user.is_active:
                raise credentials_exception

            if is_superuser and not user.is_superuser:
                raise credentials_exception

            if security_scopes.scopes:
                if not user.scopes:
                    raise credentials_exception
                if not all(scope in user.scopes for scope in security_scopes.scopes):
                    raise credentials_exception

            return SchemaUser.model_validate(user)

        return func
