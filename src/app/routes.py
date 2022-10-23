"""Подлкючение роутов для постов и пользователя"""
from fastapi import APIRouter

from .api import blog, auth


routes = APIRouter()

routes.include_router(blog.router,prefix="/blog")
routes.include_router(auth.router, prefix='/auth')
