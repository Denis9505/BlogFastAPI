from passlib.hash import bcrypt
from jose import JWTError
import jwt
from fastapi import HTTPException, status

from models.auth import User
from settings import settings


class AuthService:
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hash(password)

    @classmethod
    def validate(cls, token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authentificate': 'Bearer'
            },
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )   
        except JWTError:
            raise exception from None
