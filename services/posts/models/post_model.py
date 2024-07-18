from pydantic import BaseModel
from typing import List


class PostsModel(BaseModel):
    userId: int
    id: int
    title: str
    body: str


class AllPostsModel(BaseModel):
    posts: List[PostsModel]


class PostsCommentsModel(BaseModel):
    postId: int
    id: int
    name: str
    email: str
    body: str


class AllPostsCommentsModel(BaseModel):
    comments: List[PostsCommentsModel]
