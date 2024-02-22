import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from configs import Config

# Initialize the Pyrogram client
app = Client("my_bot")

# Reply to the user when a file is forwarded
async def reply_forward(message: Message, file_id: int):
    try:
        await message.reply_text(
            f"Files will be deleted in 30 minutes to avoid copyright issues. Please forward and save them.",
            disable_web_page_preview=True,
            quote=True
        )
    except FloodWait as e:
        await asyncio.sleep(e.x)
        await reply_forward(message, file_id)

# Forward media message to user
async def media_forward(bot: Client, user_id: int, file_id: int):
    try:
        if Config.FORWARD_AS_COPY is True:
            return await bot.copy_message(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_id=file_id)
        elif Config.FORWARD_AS_COPY is False:
            return await bot.forward_messages(chat_id=user_id, from_chat_id=Config.DB_CHANNEL, message_ids=file_id)
    except FloodWait as e:
        await asyncio.sleep(e.value)
        return media_forward(bot, user_id, file_id)

# Send media with button and reply
async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    # Get the file name
    message = await bot.get_messages(user_id, file_id)
    file_name = message.document.file_name if message.document else message.video.file_name

    # Create a button
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Click Here", url="http://example.com")]])

    # Forward the media with the button and set the caption as the file name
    sent_message = await media_forward(bot, user_id, file_id)
    await sent_message.edit_caption(file_name, reply_markup=button)

    # Delete the message after 30 minutes
    asyncio.create_task(delete_after_delay(sent_message, 1800))

# Delete a message after a delay
async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

# Start the bot
@app.on_message()
async def handle_message(client, message):
    if message.media:
        # Send media with button and reply
        await send_media_and_reply(client, message.from_user.id, message.message_id)

