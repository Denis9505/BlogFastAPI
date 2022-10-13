from fastapi import APIRouter, Depends, Response, status
from typing import List

from models.posts import CreatePost, Post, PostUpdate
from services.posts import PostsServices


router = APIRouter()


@router.get('/', response_model=List[Post])
def get_posts_list(service: PostsServices = Depends()):
    return service.get_post_list()


@router.post('/', response_model=Post)
def create_post(item: CreatePost, service: PostsServices = Depends()):
    return service.create_post(item)


@router.get('/{post_id}', response_model=Post)
def get_post(post_id:int, service: PostsServices = Depends()):
    return service.get(post_id)


@router.put('/{post_id}', response_model=Post)
def update_post(
    post_id: int,
    post_data: PostUpdate,
    service: PostsServices = Depends()
):
    return service.update_post(post_id, post_data)


@router.delete('/{post_id}')
def delete_post(post_id: int, service: PostsServices = Depends()):
    service.delite_post(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
