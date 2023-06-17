def get_user_by_id(user_id: int, endpoint='users') -> bool:
    """Check if user exists in remote database"""

    user = requests.get(f'https://jsonplaceholder.typicode.com/{endpoint}/{user_id}')
    if user and user.status_code == 200:
        return True
    return False


import requests


def get_post_by_id(post_id: int, endpoint='posts') -> dict:
    """Check if post exists in remote database"""

    post = requests.get(f'https://jsonplaceholder.typicode.com/{endpoint}/{post_id}')
    post_json = post.json()

    return post_json


if __name__ == '__main__':
    # print(get_user_by_id(0))
    # print(get_user_by_id(3))
    # print(get_user_by_id(33))

    print('yes' if get_post_by_id(334) else 'No')
    print('yes' if get_post_by_id(33) else 'No')
