from services.posts.api_post import PostsApi


class BaseTest:

    def setup_method(self):
        self.api_posts = PostsApi()
