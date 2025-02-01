from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/45b6f971145c6d52aa10e.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/45b6f971145c6d52aa10e.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Iink_ka_adda")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/CodeNexus_community")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1225278379").split()))


FAILED = "https://graph.org/file/e26bbf528594243b2e8f5.jpg"
