"""Business logic for users"""
from datetime import datetime, timedelta
from passlib.hash import bcrypt
from jose import JWTError, jwt

from fastapi import  Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from pydantic import ValidationError

from ..models.auth import Token, User, UserCreate
from ..tables import User as t_User
from ..settings import setting


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/auth/sign-in')

def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    """Get current user"""
    return AuthService.validate_token(token)


class AuthService:
    """Autorization user"""
    @classmethod
    def verify_password(cls, plain_password: str, hashed_password: str) -> bool:
        """Verify password"""
        return bcrypt.verify(plain_password, hashed_password)

    @classmethod
    def get_password_hash(cls, password: str) -> str:
        """Get password hash"""
        return bcrypt.hash(password)

    @classmethod
    def validate_token(cls, token: str) -> User:
        """Validate token"""
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
                setting.jwt_secret,
                algorithms=[setting.jwt_algorithm],
            )
        except JWTError:
            raise exception from None

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception from None

        return user

    @classmethod
    def create_token(cls, user: t_User) -> Token:
        """Create token"""
        user_data = User.from_orm(user)

        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=setting.jwt_expiration),
            'sub': str(user_data.id),
            'user': user_data.dict(),
        }
        token = jwt.encode(
            payload,
            setting.jwt_secret,
            algorithm=setting.jwt_algorithm,
        )
        return Token(access_token=token)

    def __init__(self, session:Session):
        self.session = session

    def register_new_user(self, user_data: UserCreate) -> Token:
        """Register new user"""
        user = t_User(
            email=user_data.email,
            username=user_data.username,
            password_hash=self.get_password_hash(user_data.password),
        )

        self.session.add(user)
        self.session.commit()

        return self.create_token(user)

    def authenticate_user(self, username: str, password: str) -> Token:
        """Authenticate user"""
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={
                'WWW-Authentificate': 'Bearer'
            },
        )
        user = (
            self.session
            .query(t_User)
            .filter(t_User.username == username)
            .first()
        )
        if not user:
            raise exception
        if not self.verify_password(password, user.password_hash):
            raise exception

        return self.create_token(user)
