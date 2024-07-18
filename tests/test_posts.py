import allure
from config.base_test import BaseTest


@allure.epic('Administration')
@allure.feature('Posts')
class TestPosts(BaseTest):

    @allure.title('Test GET request for post information')
    def test_get_posts(self):
        self.api_posts.get_posts()

    @allure.title('Test creating a new post by POST')
    def test_add_posts(self):
        self.api_posts.add_posts()

    @allure.title('Test editing a post by PUT')
    def test_edit_posts(self):
        self.api_posts.edit_posts()

    @allure.title('Test GET request to comment on a post')
    def test_get_comment_posts(self):
        self.api_posts.get_comment_posts()

    @allure.title('Test Deleting a post')
    def test_delete_posts(self):
        self.api_posts.delete_posts()
