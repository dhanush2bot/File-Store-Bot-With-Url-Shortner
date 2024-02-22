import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import FloodWait
from configs import Config

# Initialize the Pyrogram client
app = Client("my_bot")

# Global variables to track the number of files sent and total files
files_sent = 0
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
async def send_media_and_reply(bot: Client, user_id: int, file_id: int):
    global files_sent, total_files
    total_files += 1

    # Get the message object for the file
    message = await bot.get_messages(user_id, file_id)

    # Check if the message is a document or a video
    if message.document:
        file_name = message.document.file_name
        file_type = "document"
    elif message.video:
        file_name = message.video.file_name
        file_type = "video"
    else:
        # Handle other types of media here (e.g., audio, photo, etc.)
        return

    # Create a button
    button = InlineKeyboardMarkup([[InlineKeyboardButton("Click Here", url="http://example.com")]])

    # Forward the media with the button
    sent_message = await media_forward(bot, user_id, file_id)

    # Add the button to the media caption
    caption = f"*{file_type.capitalize()} Name:* `{file_name}`"
    await sent_message.edit_caption(caption, parse_mode="markdown", reply_markup=button)

    # Delete the message after 30 minutes
    asyncio.create_task(delete_after_delay(sent_message, 1800))

    # Increment the number of files sent
    files_sent += 1

    # Check if all files have been sent
    if files_sent == total_files:
        await reply_forward(sent_message, file_id)

# Delete a message after a delay
async def delete_after_delay(message, delay):
    await asyncio.sleep(delay)
    await message.delete()

# Start the bot
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Hello! Send me a media file and I'll forward it to you with a button.")

# Handle incoming media files
@app.on_message(filters.media)
async def handle_media(client, message):
    # Forward the media with a button and reply
    await send_media_and_reply(client, message.from_user.id, message.message_id)
