from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base



class Post(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    # user = Column(Integer, ForeignKey('users.id'))
    # user_id = relationship("User")
