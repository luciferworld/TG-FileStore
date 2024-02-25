# (c) @PredatorHackerzZ || @TeleRoidGroup

import os

class Config(object):
	API_ID = int(os.environ.get("API_ID", "25184668"))
	API_HASH = os.environ.get("API_HASH", "9de2fcd18b25deed06adf855fcd181ed")
	BOT_TOKEN = os.environ.get("BOT_TOKEN", "6992601655:AAGkcnUNIY8K7nNTthxbTZHhRp7HOgvHIQ8")
	BOT_USERNAME = os.environ.get("BOT_USERNAME", "filestoreee_bot")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1001805072460"))
	SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "")
	SHORTLINK_API = os.environ.get('SHORTLINK_API', "")
	BOT_OWNER = int(os.environ.get("BOT_OWNER", "5390385209"))
	DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Ibrahim:ibrahim@cluster0.zuppk7u.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1001934362597")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", '-1002027405917')
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659239").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS",).split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ **🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅**]────⍟
│
├🔸 **My Name:** [File Store Bot](https://t.me/{BOT_USERNAME})
│
├🔸 **Language:** [Python 3](https://www.python.org)
│
├🔹 **Library:** [Pyrogram](https://docs.pyrogram.org)
│
├🔹 **Hosted On:** [Vps](https://cloud.atlantic.net/r/cggqrw65)
│
├🔸 **Owner:** [Ibrahim](https://t.me/lucifer6985) 
│
├🔹 **File Stream bot :** [FileStream](https://t.me/Liciferfiletolink_bot)
│
├🔹 **Free Ai Logo Maker :** [LogoMaker](https://t.me/ChatGPT2112_bot?start=5390385209)
│
├🔸 **Bot Updates:** [Bots Channel](https://t.me/digitalhub04)
│
╰──────[ 😎 ]───────────⍟
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Bot owner:** [Ibrahim](https://t.me/lucifer6985)
 
 I am Super noob Please and i am not developer of this bot.

[Developer](https://t.me/DonateXrobot)
"""
	HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.

❌ **PORNOGRAPHY CONTENTS** are strictly prohibited & get Permanent Ban.
"""
