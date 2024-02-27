import asyncio
import requests
import string
import random
from configs import Config
from pyrogram import Client
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from handlers.helpers import str_to_b64

async def reply_forward(message: Message, file_id: int):
    try:
        # Send the message about file deletion
        await message.reply_text(
            f"Files will be deleted in 30 minutes to avoid copyright issues. Please forward and save them.",
            disable_web_page_preview=True,
            quote=True
        )
        # Send the message with the button for generating a stream link
        stream_message = await message.reply_text(
            "Click the button below if you want to generate a stream link",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("ᴡᴀᴛᴄʜ ᴏɴʟɪɴᴇ 👀 / ꜰᴀsᴛ ᴅᴏᴡɴʟᴏᴀᴅ 🗂️", callback_data="stream_button")]
            ])
        )
        # Delete the stream message after 30 minutes
        await asyncio.sleep(1800)  # 30 minutes
        await stream_message.delete()
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                          message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL,
                                              message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)
        await message.delete()

async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    sent_message = await media_forward(bot, user_id, file_id)
    await reply_forward(message=sent_message, file_id=file_id)
    asyncio.create_task(delete_after_delay(sent_message, 1800))

async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()
