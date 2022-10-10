from sqlalchemy.orm import Session
from .models import Post
from .shemas import CreatePost

def get_post_list(db: Session):
    return db.query(Post).all()


def create_post(db: Session, item: CreatePost):
    post = Post(**item.dict())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post
