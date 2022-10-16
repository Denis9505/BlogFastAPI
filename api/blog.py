from fastapi import APIRouter, Depends, Response, status
from typing import List

from models.posts import CreatePost, Post, PostUpdate
from models.auth import User
from services.posts import PostsServices
from services.auth import get_current_user


router = APIRouter()


@router.get('/', response_model=List[Post])
def get_posts_list(
    user: User = Depends(get_current_user),
    service: PostsServices = Depends(),
    ):
    return service.get_post_list(user_id=user.id)


@router.post('/', response_model=Post)
def create_post(
    item: CreatePost,
    user: User = Depends(get_current_user),
    service: PostsServices = Depends(),
    ):
    return service.create_post(user_id=user.id, post_data=item)


@router.get('/{post_id}', response_model=Post)
def get_post(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostsServices = Depends()
    ):
    return service.get(user_id=user.id, post_id=post_id)


@router.put('/{post_id}', response_model=Post)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    user: User = Depends(get_current_user),
    service: PostsServices = Depends()
):
    return service.update_post(user_id=user.id, post_id=post_id, post_data=post_data)


@router.delete('/{post_id}')
def delete_post(
    post_id: int,
    user: User = Depends(get_current_user),
    service: PostsServices = Depends()
    ):
    service.delite_post(user_id=user.id, post_id=post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
