from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    username: str
    # To auto convert database type to above python type
    class Config():
        orm_mode=True


class Article(BaseModel):
    title: str
    content: str
    published: bool
    # To auto convert database type to above python type
    class Config():
        orm_mode=True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id: int


class UserDisplay(BaseModel):
    username: str
    email: str
    items: List[Article] = []
    # To auto convert database type to above python type
    class Config():
        orm_mode=True


class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    # To auto convert database type to above python type
    class Config():
        orm_mode=True 