import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "MoneyKamalo.com")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0eefb93e1e3ce9470a7033115ceb1bad13a9d674")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", ""))
  DATABASE_URL = os.environ.get("DATABASE_URL", "")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", ""))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  FILE_TO_LINK_APPURL = os.environ.get("DIRECT_GEN_URL", "https://filmyspotmovie-16c4510caa97.herokuapp.com") 
  FILE_TO_LINK_LOG = int(os.environ.get("DIRECT_GEN_DB", "-1002041057749"))


  HOME_TEXT = f"""
𝑰𝒏𝒕𝒓𝒐𝒅𝒖𝒄𝒊𝒏𝒈 𝒕𝒉𝒆 𝑷𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕 𝑭𝒊𝒍𝒆𝑺𝒕𝒐𝒓𝒆 𝑩𝒐𝒕! 𝑺𝒆𝒏𝒅 𝒎𝒆 𝒂𝒏𝒚 𝒎𝒆𝒅𝒊𝒂 𝒐𝒓 𝒇𝒊𝒍𝒆, 𝒂𝒏𝒅 𝑰'𝒍𝒍 𝒔𝒕𝒐𝒓𝒆 𝒊𝒕 𝒑𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕𝒍𝒚. 𝑰 𝒄𝒂𝒏 𝒘𝒐𝒓𝒌 𝒊𝒏 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔 𝒕𝒐𝒐! 𝑨𝒅𝒅 𝒎𝒆 𝒕𝒐 𝒚𝒐𝒖𝒓 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒘𝒊𝒕𝒉 𝒆𝒅𝒊𝒕 𝒑𝒆𝒓𝒎𝒊𝒔𝒔𝒊𝒐𝒏, 𝒂𝒏𝒅 𝑰'𝒍𝒍 𝒔𝒂𝒗𝒆 𝒕𝒉𝒆 𝒖𝒑𝒍𝒐𝒂𝒅𝒆𝒅 𝒇𝒊𝒍𝒆 𝒊𝒏 𝒕𝒉𝒆 𝒄𝒉𝒂𝒏𝒏𝒆𝒍, 𝒕𝒉𝒆𝒏 𝒔𝒉𝒂𝒓𝒆 𝒂 𝒔𝒉𝒂𝒓𝒆𝒂𝒃𝒍𝒆 𝒍𝒊𝒏𝒌 𝒘𝒊𝒕𝒉 𝒚𝒐𝒖.

𝑳𝒆𝒂𝒓𝒏 𝒎𝒐𝒓𝒆 𝒂𝒃𝒐𝒖𝒕 𝒕𝒉𝒆 𝒃𝒐𝒕 𝒊𝒏 𝒕𝒉𝒆 𝑨𝒃𝒐𝒖𝒕 𝑩𝒐𝒕 𝒔𝒆𝒄𝒕𝒊𝒐𝒏.

𝑴𝒂𝒊𝒏𝒕𝒂𝒊𝒏𝒆𝒅 𝒃𝒚: [𝑭𝒊𝒍𝒎𝒚 𝑺𝒑𝒐𝒕](http://t.me/filmyspotupdate)
"""
#  ABOUT_DEV_TEXT = f"""
#🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [monster x](https://t.me/FilmySpotSupport_bot)
 
 #I am Super noob Please Support My Hard Work.

#[Donate Me](https://t.me/FilmySpotSupport_bot)
#"""
  ABOUT_BOT_TEXT  = """
𝑻𝒉𝒊𝒔 𝒊𝒔 𝒂 𝑷𝒆𝒓𝒎𝒂𝒏𝒆𝒏𝒕 𝑭𝒊𝒍𝒆𝑺𝒕𝒐𝒓𝒆 𝑩𝒐𝒕.

⇛ 𝑯𝒐𝒘 𝒕𝒐 𝑼𝒔𝒆 𝒕𝒉𝒆 𝑩𝒐𝒕 𝒂𝒏𝒅 𝑰𝒕𝒔 𝑩𝒆𝒏𝒆𝒇𝒊𝒕𝒔?

📢 𝑻𝒐 𝒖𝒔𝒆 𝒕𝒉𝒆 𝒃𝒐𝒕, 𝒋𝒖𝒔𝒕 𝒔𝒆𝒏𝒅 𝒂𝒏𝒚 𝒇𝒊𝒍𝒆, 𝒂𝒏𝒅 𝒊𝒕 𝒘𝒊𝒍𝒍 𝒃𝒆 𝒔𝒆𝒄𝒖𝒓𝒆𝒍𝒚 𝒔𝒕𝒐𝒓𝒆𝒅 𝒊𝒏 𝒎𝒚 𝒅𝒂𝒕𝒂𝒃𝒂𝒔𝒆. 𝒀𝒐𝒖'𝒍𝒍 𝒓𝒆𝒄𝒆𝒊𝒗𝒆 𝒂 𝒍𝒊𝒏𝒌 𝒕𝒐 𝒂𝒄𝒄𝒆𝒔𝒔 𝒕𝒉𝒆 𝒇𝒊𝒍𝒆.

⚠️ 𝑩𝒆𝒏𝒆𝒇𝒊𝒕𝒔: 𝑰𝒇 𝒚𝒐𝒖 𝒎𝒂𝒏𝒂𝒈𝒆 𝒂 𝑻𝒆𝒍𝒆𝒈𝒓𝒂𝒎 𝒄𝒉𝒂𝒏𝒏𝒆𝒍 𝒘𝒊𝒕𝒉 𝒎𝒐𝒗𝒊𝒆𝒔 𝒐𝒓 𝒄𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕𝒆𝒅 𝒄𝒐𝒏𝒕𝒆𝒏𝒕, 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕 𝒊𝒔 𝒑𝒆𝒓𝒇𝒆𝒄𝒕 𝒇𝒐𝒓 𝒚𝒐𝒖. 𝑺𝒂𝒇𝒆𝒍𝒚 𝒔𝒕𝒐𝒓𝒆 𝒂𝒏𝒅 𝒔𝒉𝒂𝒓𝒆 𝒇𝒊𝒍𝒆𝒔 𝒘𝒊𝒕𝒉𝒐𝒖𝒕 𝒂𝒏𝒚 𝒓𝒊𝒔𝒌 𝒐𝒇 𝒄𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝒊𝒏𝒇𝒓𝒊𝒏𝒈𝒆𝒎𝒆𝒏𝒕. 𝑰 𝒂𝒍𝒔𝒐 𝒔𝒖𝒑𝒑𝒐𝒓𝒕 𝒄𝒉𝒂𝒏𝒏𝒆𝒍𝒔!.

𝑴𝒚 𝑵𝒂𝒎𝒆: [𝑭𝒊𝒍𝒆𝑺𝒕𝒐𝒓𝒆 𝑩𝒐𝒕](https://t.me/{BOT_USERNAME})
𝑳𝒂𝒏𝒈𝒖𝒂𝒈𝒆: [𝑷𝒚𝒕𝒉𝒐𝒏 3](https://www.python.org)
𝑳𝒊𝒃𝒓𝒂𝒓𝒚: [𝑷𝒚𝒓𝒐𝒈𝒓𝒂𝒎](https://docs.pyrogram.org)

"""
