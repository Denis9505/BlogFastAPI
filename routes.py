from fastapi import APIRouter

from api import blog


routes = APIRouter()

routes.include_router(blog.router,prefix="/blog")