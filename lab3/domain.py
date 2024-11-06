# baza danych
import aiohttp
from dataclasses import dataclass

URL = 'https://jsonplaceholder.typicode.com/posts'

@dataclass
class PostRecord:
    userId: int
    id: int
    title: str
    body: str


class PostDB:
    async def init_db(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                self.posts = await response.json()
