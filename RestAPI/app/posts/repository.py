# app/posts/repository.py
from sqlalchemy.ext.asyncio import AsyncSession
from app.posts.models import Post
from sqlalchemy import select
from typing import Optional


class PostRepository:
    def __init__(self, session:AsyncSession):
        self.session = session


    # 비동기여야함
    async  def save(self, post : Post) -> Post:
        self.session.add(post)
        # await self.session.commit() # 서비스에서 해야함
        await self.session.refresh(post)
        return post

    '''async def find_by_id(self, post : Post) -> type[Post] | None:
        result = await self.session.get(Post, post.id)
        return result'''

    async def find_by_id(self, target_id:int)-> Optional[Post]:
        query = select(Post).where(Post.id == target_id)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def delete(self, post : Post) -> Post:
        await self.session.delete(post)
        await self.session.flush()
        return post


