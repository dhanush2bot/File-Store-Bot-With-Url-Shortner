import os
import asyncio
import traceback
import binascii
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, Message
from configs import Config
from handlers.database import db
from handlers.add_user_to_db import add_user_to_database
from handlers.send_file import send_media_and_reply
from handlers.helpers import b64_to_str, str_to_b64
from handlers.check_user_status import handle_user_status
from handlers.force_sub_handler import handle_force_sub, get_invite_link
from handlers.broadcast_handlers import main_broadcast_handler
from handlers.save_media import save_media_in_channel, save_batch_media_in_channel

MediaList = {}

Bot = Client(
    name=Config.BOT_USERNAME,
    in_memory=True,
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

@Bot.on_message(filters.private)
async def handle_private_message(bot: Client, cmd: Message):
    await handle_user_status(bot, cmd)

@Bot.on_message(filters.command("start") & filters.private)
async def start(bot: Client, cmd: Message):
    if cmd.from_user.id in Config.BANNED_USERS:
        await cmd.reply_text("Sorry, You are banned.")
        return
    if Config.UPDATES_CHANNEL is not None:
        back = await handle_force_sub(bot, cmd)
        if back == 400:
            return
    usr_cmd = cmd.text.split("_", 1)[-1]
    if usr_cmd == "/start":
        await add_user_to_database(bot, cmd)
        await cmd.reply_text(
            Config.HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("• Updates Channel •", url="https://t.me/filmyspotupdate")],
                    [InlineKeyboardButton("• About Bot", callback_data="aboutbot"),
                     InlineKeyboardButton("Support •", url="https://t.me/FilmySpotSupport_bot")],
                    [InlineKeyboardButton("• Movie Request Group", url=" https://t.me/+o_VcAI8GRQ8zYzA9"),
                     InlineKeyboardButton("Movie Channel •", url="https://t.me/filmyspotmovie")],
                    [InlineKeyboardButton("• Close •", callback_data="closeMessage")]
                ]
            )
        )
    else:
        try:
            try:
                file_id = int(b64_to_str(usr_cmd).split("_")[-1])
            except (binascii.Error, UnicodeDecodeError):
                file_id = int(usr_cmd.split("_")[-1])
            GetMessage = await bot.get_messages(chat_id=Config.DB_CHANNEL, message_ids=file_id)
            message_ids = []
            if GetMessage.text:
                message_ids = GetMessage.text.split(" ")
                _response_msg = await cmd.reply_text(
                    text=f"**Total Files:** `{len(message_ids)}`",
                    quote=True,
                    disable_web_page_preview=True
                )
            else:
                message_ids.append(int(GetMessage.id))
            for i in range(len(message_ids)):
                await send_media_and_reply(bot, user_id=cmd.from_user.id, file_id=int(message_ids[i]))
        except Exception as err:
            await cmd.reply_text(f"Something went wrong!\n\n**Error:** `{err}`")

@Bot.on_message((filters.document | filters.video | filters.audio | filters.photo) & ~filters.chat(Config.DB_CHANNEL))
async def handle_media_message(bot: Client, message: Message):
    if message.chat.type == "private":
        await add_user_to_database(bot, message)
        if Config.UPDATES_CHANNEL is not None:
            back = await handle_force_sub(bot, message)
            if back == 400:
                return
        if message.from_user.id in Config.BANNED_USERS:
            await message.reply_text("Sorry, You are banned!\n\nContact [Support](https://t.me/FilmySpotSupport_bot)",
                                     disable_web_page_preview=True)
            return
        if not Config.OTHER_USERS_CAN_SAVE_FILE:
            return
        await message.reply_text(
            text="**Choose an option from below:**",
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("• Save in Batch •", callback_data="addToBatchTrue")],
                [InlineKeyboardButton("• Save Direct Link •", callback_data="addToBatchFalse")]
            ]),
            quote=True,
            disable_web_page_preview=True
        )
    elif message.chat.type == "channel":
        if (message.chat.id == int(Config.LOG_CHANNEL)) or (message.chat.id == int(Config.UPDATES_CHANNEL)) or message.forward_from_chat or message.forward_from:
            return
        elif int(message.chat.id) in Config.BANNED_CHAT_IDS:
            await bot.leave_chat(message.chat.id)
            return
        else:
            pass
        try:
            forwarded_msg = await message.forward(Config.DB_CHANNEL)
            file_er_id = str(forwarded_msg.id)
            share_link = f"https://t.me/{Config.BOT_USERNAME}?start=filmyspot_{str_to_b64(file_er_id)}"
            CH_edit = await bot.edit_message_reply_markup(message.chat.id, message.id,
                                                          reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(
                                                              "Get Sharable Link", url=share_link)]]))
            if message.chat.username:
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/{message.chat.username}/{CH_edit.id}) Channel's Broadcasted File's Button Added!")
            else:
                private_ch = str(message.chat.id)[4:]
                await forwarded_msg.reply_text(
                    f"#CHANNEL_BUTTON:\n\n[{message.chat.title}](https://t.me/c/{private_ch}/{CH_edit.id}) Channel's Broadcasted File's Button Added!")
        except Exception as error:
            try:
                await message.reply_text(f"Got Error `{error}`\n\nFor Support [Support](https://t.me/FilmySpotSupport_bot)",
                                         disable_web_page_preview=True)
            except Exception as new_error:
                print(f"unable to send message due to {new_error}")

@Bot.on_callback_query(filters.regex(pattern=r"closeMessage"))
async def close_message(bot: Client, cmd: CallbackQuery):
    await cmd.message.delete()

@Bot.on_callback_query(filters.regex(pattern=r"aboutbot"))
async def about_bot(bot: Client, cmd: CallbackQuery):
    await cmd.message.edit(
        text=Config.ABOUT_TEXT,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("Close", callback_data="closeMessage")]
            ]
        )
    )

@Bot.on_callback_query(filters.regex(pattern=r"addToBatchTrue"))
async def add_to_batch_true(bot: Client, cmd: CallbackQuery):
    if cmd.message.chat.type == "private":
        await cmd.message.delete()
        await cmd.message.reply_text(
            text="**Send me the files you want to save in batch!**\n\n*Note: To stop, send* `/cancel`.",
            quote=True
        )
        MediaList[cmd.from_user.id] = []

@Bot.on_callback_query(filters.regex(pattern=r"addToBatchFalse"))
async def add_to_batch_false(bot: Client, cmd: CallbackQuery):
    if cmd.message.chat.type == "private":
        await cmd.message.delete()
        await cmd.message.reply_text(
            text="**Send me the file you want to save directly!**",
            quote=True
        )

@Bot.on_message(filters.command("cancel") & filters.private)
async def cancel_command(bot: Client, cmd: Message):
    if cmd.from_user.id in MediaList:
        del MediaList[cmd.from_user.id]
        await cmd.reply_text("Operation canceled successfully!")

@Bot.on_message(filters.chat(Config.DB_CHANNEL) & (filters.document | filters.video | filters.audio | filters.photo))
async def save_media_in_db(bot: Client, message: Message):
    try:
        if message.media:
            if message.media.document:
                await save_media_in_channel(bot, message, message.media.document.file_id)
            elif message.media.video:
                await save_media_in_channel(bot, message, message.media.video.file_id)
            elif message.media.audio:
                await save_media_in_channel(bot, message, message.media.audio.file_id)
            elif message.media.photo:
                await save_media_in_channel(bot, message, message.media.photo.file_id)
    except Exception as error:
        print(f"An error occurred: {error}")

@Bot.on_callback_query()
async def button(bot: Client, cmd: CallbackQuery):
    cb_data = cmd.data
    if cb_data.startswith("ban_user_"):
        user_id = int(cb_data.split("_")[-1])
        Config.BANNED_USERS.append(user_id)
        await cmd.answer("User banned successfully!")
        await cmd.message.delete()
    elif cb_data.startswith("cancelBatch_"):
        user_id = int(cb_data.split("_")[-1])
        if user_id in MediaList:
            del MediaList[user_id]
            await cmd.answer("Batch operation canceled successfully!")
        await cmd.message.delete()

async def main():
    await Bot.start()
    print("Bot Started!")
    await main_broadcast_handler(Bot, db=db)  # Pass the `db` argument here
    await Bot.idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
