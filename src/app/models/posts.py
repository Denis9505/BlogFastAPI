"""Post model"""
from datetime import date
from pydantic import BaseModel# pylint: disable=no-name-in-module



class PostBase(BaseModel):# pylint: disable=too-few-public-methods
    """Basic post model"""
    title: str
    text: str
    date: date


class Post(PostBase):# pylint: disable=too-few-public-methods
    """Getting post"""
    id: int

    class Config:# pylint: disable=too-few-public-methods
        """Orm mode"""
        orm_mode=True


class CreatePost(PostBase):# pylint: disable=too-few-public-methods
    """Create post model"""


class PostUpdate(PostBase):# pylint: disable=too-few-public-methods
    """Update post model"""
