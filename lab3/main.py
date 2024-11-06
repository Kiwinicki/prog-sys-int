import asyncio
from domain import PostDB
from service import PostService
from repository import PostRepository

async def main() -> None:
    db = PostDB()
    await db.init_db()
    repo = PostRepository(domain=db)
    service = PostService(repository=repo)
    posts_by_title = service.filter_by_title('magnam')
    posts_by_body = service.filter_by_body('et iusto')
    print(posts_by_title)
    print(posts_by_body)



if __name__ == "__main__":
    asyncio.run(main())