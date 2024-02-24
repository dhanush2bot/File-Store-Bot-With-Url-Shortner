import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from configs import Config

# Initialize the Pyrogram client
app = Client("my_bot")

# Reply to the user when a file is forwarded
async def reply_forward(message: Message, file_id: int):
    await asyncio.sleep(0.1)
    await message.reply_text(
        "Files will be deleted in 30 minutes to avoid copyright issues. Please forward and save them.",
        disable_web_page_preview=True,
        quote=True,
    )

# Forward media message to user
async def media_forward(bot: Client, user_id: int, file_id: int):
    return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)

# Send media with button and reply
async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    try:
        sent_message = await media_forward(bot, user_id, file_id)
        caption = sent_message.caption.markdown if sent_message.caption else ""
        button = InlineKeyboardMarkup([[InlineKeyboardButton("Watch Online / Fast Download", callback_data="stream_button")]])
        await sent_message.edit_caption(caption, reply_markup=button)
        await reply_forward(sent_message, file_id)
        asyncio.create_task(delete_after_delay(sent_message, 1800))
    except Exception as e:
        print(f"Error: {e}")

# Delete a message after a delay
async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

# Start the bot
@app.on_message()
async def handle_message(client, message):
    if message.media:
        await send_media_and_reply(client, message.from_user.id, message.message_id)

