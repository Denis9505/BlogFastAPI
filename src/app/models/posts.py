from pydantic import BaseModel
from datetime import date


class PostBase(BaseModel):
    title: str
    text: str
    date: date


class Post(PostBase):
    id: int

    class Config:
        orm_mode=True


class CreatePost(PostBase):
    pass


class PostUpdate(PostBase):
    pass
