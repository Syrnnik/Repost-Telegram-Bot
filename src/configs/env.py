import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
VK_APP_ACCESS_TOKEN = os.getenv("VK_APP_ACCESS_TOKEN")
VK_GROUP_ACCESS_TOKEN = os.getenv("VK_GROUP_ACCESS_TOKEN")
VK_GROUP_TAG = os.getenv("VK_GROUP_TAG")
VK_GROUP_ID = os.getenv("VK_GROUP_ID")
TG_CHANNEL_ID = os.getenv("TG_CHANNEL_ID")
