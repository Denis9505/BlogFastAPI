"""Api urls and views for posts"""
from typing import List
from fastapi import APIRouter, Depends, Response, HTTPException, status
from sqlalchemy.orm import Session

from database import get_session
from models.posts import CreatePost, Post, PostUpdate
from models.auth import User
from services.posts import PostsServices
from api.auth import get_current_user


router = APIRouter()


@router.get('/', response_model=List[Post])
def get_posts_list(
    user: User = Depends(get_current_user),
    session: Session=Depends(get_session),
    ):
    """Getting a list of posts"""
    service = PostsServices(session=session)
    return service.get_post_list(user_id=user.id)


@router.post('/', response_model=Post)
def create_post(
    item: CreatePost,
    user: User = Depends(get_current_user),
    session: Session=Depends(get_session)
    ):
    """Create post"""
    service = PostsServices(session=session)
    return service.create_post(user_id=user.id, post_data=item)


@router.get('/{post_id}', response_model=Post)
def get_post(
    post_id: int,
    user: User = Depends(get_current_user),
    session: Session=Depends(get_session)
    ):
    """Getting one post"""
    service = PostsServices(session=session)
    post = service.get(user_id=user.id, post_id=post_id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post


@router.put('/{post_id}', response_model=Post)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    user: User = Depends(get_current_user),
    session: Session=Depends(get_session)
):
    """Update post"""
    service = PostsServices(session=session)
    res = service.update_post(user_id=user.id, post_id=post_id, post_data=post_data)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return res


@router.delete('/{post_id}')
def delete_post(
    post_id: int,
    user: User = Depends(get_current_user),
    session: Session=Depends(get_session)
    ):
    """Delete post"""
    service = PostsServices(session=session)
    service.delite_post(user_id=user.id, post_id=post_id)
    res = Response(status_code=status.HTTP_204_NO_CONTENT)
    if not res:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return res
