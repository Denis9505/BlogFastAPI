"""Model user"""
from pydantic import BaseModel# pylint: disable=no-name-in-module


class BaseUser(BaseModel):# pylint: disable=too-few-public-methods
    """Basic user model"""
    email: str
    username: str


class UserCreate(BaseUser):# pylint: disable=too-few-public-methods
    """Create user"""
    password: str


class User(BaseUser):# pylint: disable=too-few-public-methods
    """Getting user"""
    id: int

    class Config:# pylint: disable=too-few-public-methods
        """Orm mode"""
        orm_mode = True


class Token(BaseModel):# pylint: disable=too-few-public-methods
    """Token model"""
    access_token: str
    token_type: str = 'bearer'
