from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "11447635"))
API_HASH = getenv("API_HASH", "fd48e41738daae23b21d25610448da3c")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","𝘿𝙊𝙊𝙕𝙔 𝙓 𝙈𝙐𝙎𝙄𝘾 𝘽𝙊𝙏")
BOT_USERNAME = getenv("BOT_USERNAME", "doozy_X_Music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "DHANANJAYA_OFFICIALLY")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "s_e_e_me")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "999"))
START_IMG = getenv("START_IMG", "https://telegra.ph/file/1a1e45687f12d6d2d2cc7.jpg")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/1a1e45687f12d6d2d2cc7.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5577264457").split()))
