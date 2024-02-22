import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from configs import Config

# Initialize the Pyrogram client
app = Client("my_bot")

# Reply to the user when a file is forwarded
# Reply to the user with the warning message and the button
async def reply_forward(message: Message, file_id: int):
    try:
        # Create the button
        button = InlineKeyboardMarkup([[InlineKeyboardButton("Click Here", url="http://example.com")]])

        # Wait for 0.3 seconds
        await asyncio.sleep(0.3)

        # Reply with the warning message and the button
        await message.reply_text(
            f"Files will be deleted in 30 minutes to avoid copyright issues. Please forward and save them.",
            disable_web_page_preview=True,
            quote=True,
            reply_markup=button
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
    try:
        # Forward the media
        sent_message = await media_forward(bot, user_id, file_id)

        # Add the button to the existing caption
        caption = sent_message.caption.markdown if sent_message.caption else ""
        button = InlineKeyboardMarkup([[InlineKeyboardButton("Click Here", url="http://example.com")]])
        await sent_message.edit_caption(caption, reply_markup=button)

        # Add the warning message as a reply to the media
        await reply_forward(sent_message, file_id)

        # Delete the message after 30 minutes
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
        # Send media with button and reply
        await send_media_and_reply(client, message.from_user.id, message.message_id)

