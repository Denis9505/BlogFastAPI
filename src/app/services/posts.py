from typing import List
from sqlalchemy.orm import Session

from tables import Post
from models.posts import CreatePost, PostUpdate


class PostsServices:
    
    def __init__(self, session: Session):
        self.session = session

    def _get(self, user_id: int, post_id: int) -> Post:
        return (
            self.session
            .query(Post)
            .filter_by(id=post_id, user_id=user_id)
            .first()
        )


    def get_post_list(self, user_id: int) -> List[Post]:
        return (
            self.session
            .query(Post)
            .filter_by(user_id=user_id)
            .all()
        )

    def get(self, user_id: int, post_id: int) -> Post:
        return self._get(user_id, post_id)

    def create_post(self, user_id: int, post_data: CreatePost) -> Post:
        post = Post(**post_data.dict(), user_id=user_id)
        self.session.add(post)
        self.session.commit()
        return post

    def update_post(self, user_id: int, post_id: int, post_data: PostUpdate):
        post = self._get(user_id, post_id)
        for field, value in post_data:
            setattr(post, field, value)
        self.session.commit()
        return post

    def delite_post(self, user_id: int, post_id: int):
        post = self._get(user_id, post_id)
        self.session.delete(post)
        self.session.commit()
