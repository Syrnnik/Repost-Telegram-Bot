import asyncio

from aiogram import Bot
from vk_api.bot_longpoll import VkBotEventType

from configs.loader import dp, bot, long_poll
from utils.get_latest_post_data import get_latest_post_data
from utils.send_post_to_telegram import send_post_to_telegram


async def on_startup(bot: Bot):
    bot_data = await bot.me()
    print(f"{bot_data.first_name} is ready!")

    for event in long_poll.listen():
        if event.type == VkBotEventType.WALL_POST_NEW:
            post_text, post_photos = get_latest_post_data()
            await send_post_to_telegram(post_text, post_photos)


async def main():
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
