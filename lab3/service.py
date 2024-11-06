# logika biznesowa
from domain import PostRecord
from repository import PostRepository

class PostService:
    def __init__(self, repository: PostRepository):
        self.repository = repository

    def filter_by_title(self, substr: str):
        posts = self.repository.get_all_posts()
        matching_posts = filter(lambda p: substr in p['title'], posts)
        return matching_posts

    def filter_by_body(self, substr: str):
        posts = self.repository.get_all_posts()
        matching_posts = filter(lambda p: substr in p['body'], posts)