# query DB

from domain import PostRecord

class PostRepository:
    def __init__(self, domain):
        self.domain = domain

    def get_all_posts(self) -> list[PostRecord]:
        return self.domain.posts
