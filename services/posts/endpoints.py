
HOST = "https://jsonplaceholder.typicode.com"


class Endpoints:

    get_posts = f'{HOST}/posts'

    @staticmethod
    def get_post_by_id(post_id) -> str:
        get_post_by_id_endpoints = f'{HOST}/posts/{post_id}'
        return get_post_by_id_endpoints

    add_post = f'{HOST}/posts'

    @staticmethod
    def put_post_by_id(post_id) -> str:
        put_post_by_id_endpoints = f'{HOST}/posts/{post_id}'
        return put_post_by_id_endpoints

    @staticmethod
    def get_comment_post_by_id(post_id) -> str:
        comment_post_by_id_endpoints = f'{HOST}/posts/{post_id}/comments'
        return comment_post_by_id_endpoints

    delete_post = f'{HOST}/posts/1'
