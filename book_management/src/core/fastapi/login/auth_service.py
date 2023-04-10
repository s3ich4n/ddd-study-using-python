from datetime import timedelta, datetime
from typing import Union

from dependency_injector.providers import Configuration
from jose import jwt
from passlib.context import CryptContext


class AuthService:
    def __init__(
            self,
            security_config: Configuration,
    ) -> None:
        self.security_config = security_config
        self._context = self.create_crypt_context()

    def create_crypt_context(self):
        return CryptContext(
            schemes=[f"{self.security_config.get('PASSWORD_ALGORITHMS')}"],
            deprecated="auto",
        )

    def hash_password(
            self,
            value: str,
    ) -> str:
        return str(self._context.hash(value))

    def verify(
            self,
            value: str,
            hashed: str,
    ) -> bool:
        return bool(self._context.verify(value, hashed))

    def _encode_token(
            self,
            data: dict,
            expires_delta: Union[timedelta, None] = None,
    ):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.now() + expires_delta
        else:
            expire = datetime.now() + timedelta(minutes=15)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            to_encode,
            self.security_config.get("JWT_SECRET"),
            algorithm=self.security_config.get("JWT_ALGORITHMS"),
        )

        return {
            "access_token": encoded_jwt,
            "exp": int(expire.strftime("%s")),
        }

    def create_token(
            self,
            user: 'Credentials',    # fixme 순환참조 구조 해결해야함
    ):
        access_token_expires = timedelta(
            minutes=self.security_config.get("ACCESS_TOKEN_EXPIRE_MINUTES"),
        )
        token = self._encode_token(
            data={"sub": user.username},
            expires_delta=access_token_expires,
        )

        return token
