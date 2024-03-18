from configs.env import VK_GROUP_TAG
from configs.loader import vk_app
from utils.get_post_photos import get_post_photos


def get_latest_post_data():
    response = vk_app.wall.get(domain=VK_GROUP_TAG, count=1)
    post = response['items'][0]
    post_text: str = post['text']
    post_photos = get_post_photos(post)
    return post_text, post_photos
