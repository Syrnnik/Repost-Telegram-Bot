from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll

from configs.env import BOT_TOKEN, VK_GROUP_ACCESS_TOKEN, VK_APP_ACCESS_TOKEN, VK_GROUP_ID

bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

vk_bot_session = VkApi(token=VK_GROUP_ACCESS_TOKEN)
vk_bot = vk_bot_session.get_api()

vk_app_session = VkApi(token=VK_APP_ACCESS_TOKEN)
vk_app = vk_app_session.get_api()

long_poll = VkBotLongPoll(vk_bot_session, group_id=VK_GROUP_ID)
