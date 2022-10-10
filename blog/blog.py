from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from core.utils import get_db
from blog import service
from .shemas import CreatePost, PostList



router = APIRouter()


@router.get('/', response_model=List[PostList])
def post_list(db: Session = Depends(get_db)):
    return service.get_post_list(db)


@router.post('/')
def create_post(item: CreatePost, db: Session = Depends(get_db)):
    return service.create_post(db, item)
