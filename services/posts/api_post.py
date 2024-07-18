import allure
import requests
from utils.helper import Helper
from services.posts.payloads import Payloads
from services.posts.endpoints import Endpoints
from config.headers import Headers
from services.posts.models.post_model import *
import time
from http import HTTPStatus


class PostsApi(Helper):

    def __init__(self):
        super().__init__()
        self.payloads = Payloads()
        self.endpoints = Endpoints()
        self.headers = Headers()

    @allure.step('GET request for post information')
    def get_posts(self):
        start_time = time.time()
        response = requests.get(
            url=self.endpoints.get_posts,
            headers=self.headers.content_type
        )
        end_time = time.time()
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_time(start_time, end_time)
        self.attach_response(response.json())
        model = AllPostsModel(posts=response.json())
        return model

    @allure.step('Creating a new post by POST')
    def add_posts(self):
        start_time = time.time()
        response = requests.post(
            url=self.endpoints.add_post,
            headers=self.headers.content_type,
            json=self.payloads.add_post
        )
        end_time = time.time()
        assert response.status_code == HTTPStatus.CREATED, response.json()
        self.attach_time(start_time, end_time)
        self.attach_response(response.json())
        self.attach_request(response.request.body)
        model = PostsModel(**response.json())
        return model

    @allure.step('Editing a post by PUT')
    def edit_posts(self):
        start_time = time.time()
        response = requests.put(
            url=self.endpoints.put_post_by_id(1),
            headers=self.headers.content_type,
            json=self.payloads.update_post
        )
        end_time = time.time()
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_time(start_time, end_time)
        self.attach_response(response.json())
        self.attach_request(response.request.body)
        model = PostsModel(**response.json())
        return model

    @allure.step('GET request to comment on a post')
    def get_comment_posts(self):
        start_time = time.time()
        response = requests.get(
            url=self.endpoints.get_comment_post_by_id(1),
            headers=self.headers.content_type,
        )
        end_time = time.time()
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_time(start_time, end_time)
        self.attach_response(response.json())
        model = AllPostsCommentsModel(comments=response.json())
        return model

    @allure.step('Deleting a post')
    def delete_posts(self):
        start_time = time.time()
        response = requests.get(
            url=self.endpoints.delete_post,
            headers=self.headers.content_type,
        )
        end_time = time.time()
        assert response.status_code == HTTPStatus.OK, response.json()
        self.attach_time(start_time, end_time)
