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
  # Bot pics
  PICS = (os.environ.get('PICS', 'https://graph.org/file/ca175c67010e486e296f1.jpg')).split()

  # stream features vars
  FILE_TO_LINK_APPURL = os.environ.get("DIRECT_GEN_URL", "https://filmyspotmovie-16c4510caa97.herokuapp.com") 
  FILE_TO_LINK_LOG = int(os.environ.get("DIRECT_GEN_DB", "-1002041057749"))

  HOME_TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴏᴜʀ ᴘᴇʀᴍᴀɴᴇɴᴛ ғɪʟᴇꜱᴛᴏʀᴇ ʙᴏᴛ! 

ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ᴍᴇᴅɪᴀ ᴏʀ ғɪʟᴇ, ᴀɴᴅ ɪ'ʟʟ ᴛᴀᴋᴇ ᴄᴀʀᴇ ᴏғ ɪᴛ ғᴏʀ ʏᴏᴜ. ɪ ᴄᴀɴ ᴇᴠᴇɴ ᴡᴏʀᴋ ɪɴ ᴄʜᴀɴɴᴇʟꜱ! ɪᴜꜱᴛ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴇᴅɪᴛ ᴘᴇʀᴍɪꜱꜱɪᴏɴ, ᴀɴᴅ ɪ'ʟʟ ꜱᴀᴠᴇ ᴛʜᴇ ᴜᴘʟᴏᴀᴅᴇᴅ ғɪʟᴇ ᴀɴᴅ ꜱʜᴀʀᴇ ᴀ ʟɪɴᴋ ᴛʜᴀᴛ'ꜱ ᴇᴀꜱʏ ᴛᴏ ꜱʜᴀʀᴇ ᴡɪᴛʜ ᴏᴛʜᴇʀꜱ.

"""
  SOURCE_CODE = f"""
↪ ᴛʜɪꜱ ʙᴏᴛ ᴜꜱᴇꜱ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ

↪ ᴡɪᴛʜ ᴀʙᴏᴜᴛ 𝟿𝟶% ᴏғ ᴛʜᴇ ᴄᴏᴅᴇ ʙᴇɪɴɢ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ᴀɴᴅ ᴛʜᴇ ʀᴇᴍᴀɪɴɪɴɢ 𝟷𝟶% ᴘʀɪᴠᴀᴛᴇ. ɪғ ʏᴏᴜ ᴡᴀɴᴛ ᴀ ꜱɪᴍɪʟᴀʀ ʙᴏᴛ, ʏᴏᴜ ᴄᴀɴ ᴇᴀꜱɪʟʏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ ғʀᴏᴍ ᴏᴜʀ ᴏᴘᴇɴ ꜱᴏᴜʀᴄᴇ ɢɪᴛʜᴜʙ ʀᴇᴘᴏꜱɪᴛᴏʀʏ. 
↪ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟꜱ, ᴄᴏɴᴛᴀᴄᴛ ᴛʜᴇ ᴀᴅᴍɪɴ. 
"""
  ABOUT_BOT_TEXT = """

📢 𝐇𝐨𝐰 𝐭𝐨 𝐔𝐬𝐞 𝐅𝐢𝐥𝐞𝐒𝐭𝐨𝐫𝐞 𝐁𝐨𝐭 & 𝐈𝐭𝐬 𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬  📢

𝐒𝐞𝐧𝐝 𝐚𝐧𝐲 𝐅𝐢𝐥𝐞: ꜱᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ, ᴀɴᴅ ɪᴛ ᴡɪʟʟ ʙᴇ ꜱᴇᴄᴜʀᴇʟʏ ᴜᴘʟᴏᴀᴅᴇᴅ ᴛᴏ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ. ʏᴏᴜ ᴡɪʟʟ ʀᴇᴄᴇɪᴠᴇ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ ᴛᴏ ᴀᴄᴄᴇꜱꜱ ᴛʜᴇ ғɪʟᴇ.

𝐁𝐞𝐧𝐞𝐟𝐢𝐭𝐬: ɪғ ʏᴏᴜ ʜᴀᴠᴇ ᴀ ᴛᴇʟᴇɢʀᴀᴍ ᴍᴏᴠɪᴇ ᴄʜᴀɴɴᴇʟ ᴏʀ ᴀɴʏ ᴄʜᴀɴɴᴇʟ ᴡɪᴛʜ ᴄᴏᴘʏʀɪɢʜᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ, ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ᴘᴇʀғᴇᴄᴛ ғᴏʀ ᴅᴀɪʟʏ ᴜꜱᴇ. ʏᴏᴜ ᴄᴀɴ ꜱᴇɴᴅ ᴍᴇ ʏᴏᴜʀ ғɪʟᴇꜱ, ᴀɴᴅ ɪ ᴡɪʟʟ ᴘʀᴏᴠɪᴅᴇ ʏᴏᴜ ᴡɪᴛʜ ᴀ ᴘᴇʀᴍᴀɴᴇɴᴛ ʟɪɴᴋ, ᴇɴꜱᴜʀɪɴɢ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ɪꜱ ꜱᴀғᴇ ғʀᴏᴍ ᴄᴏᴘʏʀɪɢʜᴛ ɪɴғʀɪɴɢᴇᴍᴇɴᴛ ɪꜱꜱᴜᴇꜱ.

𝐒𝐮𝐩𝐩𝐨𝐫𝐭𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥𝐬: ɪ ꜱᴜᴘᴘᴏʀᴛ ᴄʜᴀɴɴᴇʟ ᴜᴘʟᴏᴀᴅꜱ ᴛᴏᴏ!

◈ ᴠᴇʀꜱɪᴏɴ: ᴠ𝟷.𝟸
◈ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ: [ᴍᴏɴꜱᴛᴇʀ x](https://t.me/FilmySpotSupport_bot) 
◈ ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: [ғɪʟᴍ ꜱᴘᴏᴛ](https://t.me/filmyspotupdate)

𝐀𝐝𝐝𝐢𝐭𝐢𝐨𝐧𝐚𝐥 𝐅𝐞𝐚𝐭𝐮𝐫𝐞: ᴛʜɪꜱ ʙᴏᴛ ɪꜱ ɴᴏᴛ ɪᴜꜱᴛ ᴀ ғɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ. ʏᴏᴜ ᴄᴀɴ ᴀʟꜱᴏ ɢᴇɴᴇʀᴀᴛᴇ ꜱᴛʀᴇᴀᴍɪɴɢ ʟɪɴᴋꜱ ᴜꜱɪɴɢ ᴛʜɪꜱ ʙᴏᴛ.

◈ ʙᴏᴛ ɴᴀᴍᴇ: [ғɪʟᴇꜱᴛᴏʀᴇ ʙᴏᴛ](https://t.me/{BOT_USERNAME})
◈ ʟᴀɴɢᴜᴀɢᴇ: [ᴘʏᴛʜᴏɴ 𝟹](https://www.python.org)
◈ ʟɪʙʀᴀʀʏ: [ᴘʏʀᴏɢʀᴀᴍ](https://docs.pyrogram.org)

⇛ Fᴏʀ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ, ᴄʟɪᴄᴋ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ.

"""

