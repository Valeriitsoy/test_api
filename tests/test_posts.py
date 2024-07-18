import allure
import pytest
from config.base_test import BaseTest


@allure.epic('Administration')
@allure.feature('Posts')
class TestPosts(BaseTest):

    @allure.title('Test GET request for post information')
    @pytest.mark.smoke
    def test_get_posts(self):
        self.api_posts.get_posts()

    @allure.title('Test creating a new post by POST')
    @pytest.mark.smoke
    def test_add_posts(self):
        self.api_posts.add_posts()

    @allure.title('Test editing a post by PUT')
    @pytest.mark.regress
    def test_edit_posts(self):
        self.api_posts.edit_posts()

    @allure.title('Test GET request to comment on a post')
    @pytest.mark.regress
    def test_get_comment_posts(self):
        self.api_posts.get_comment_posts()

    @allure.title('Test Deleting a post')
    @pytest.mark.regress
    def test_delete_posts(self):
        self.api_posts.delete_posts()
