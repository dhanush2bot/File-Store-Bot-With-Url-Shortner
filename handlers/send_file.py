import asyncio
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from configs import Config

# Initialize the Pyrogram client
app = Client("my_bot")

# Global variable to track the number of received files
received_files = 0
total_files = 0

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
async def send_media_and_reply(bot: Client, user_id: int, file_id: int, total_files: int):
    # Forward the media with the button
    sent_message = await media_forward(bot, user_id, file_id)

    # Add the button to the media caption
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Click Here", url="http://example.com")]])
    await sent_message.edit_caption("", reply_markup=button)

    # Delete the message after 30 minutes
    asyncio.create_task(delete_after_delay(sent_message, 1800))

    # Check if all files have been received
    global received_files
    received_files += 1
    if received_files == total_files:
        # Send the final message
        await reply_forward(sent_message, file_id)

# Delete a message after a delay
async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

# Start the bot
@app.on_message()
async def handle_message(client, message):
    if message.media:
        # Assuming you have the total_files count stored in a variable called total_files
        await send_media_and_reply(client, message.from_user.id, message.message_id, total_files)

