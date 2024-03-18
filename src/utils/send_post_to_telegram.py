from aiogram.types import InputMediaPhoto

from configs.env import TG_CHANNEL_ID
from configs.loader import bot


async def send_post_to_telegram(text: str, photos: list):
    if len(photos) == 0:
        await bot.send_message(
            chat_id=TG_CHANNEL_ID,
            text=text
        )

    else:
        medias = []
        for index, photo in enumerate(photos):
            media = InputMediaPhoto(media=photo)
            if index == 0:
                media = InputMediaPhoto(media=photo, caption=text)
            medias.append(media)

        await bot.send_media_group(
            chat_id=TG_CHANNEL_ID,
            media=medias,
        )
