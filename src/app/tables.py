from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password_hash = Column(String)


class Post(Base):
    __tablename__ = 'blog_posts'

    id = Column(Integer, primary_key=True, index=True, unique=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    title = Column(String)
    text = Column(Text)
    date = Column(DateTime)
    user = relationship('User')
