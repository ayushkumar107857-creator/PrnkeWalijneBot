import re
from os import environ

# -------------------------
# Helper
# -------------------------
def str_to_bool(val, default=False):
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes", "on")

# =========================================================
# 🤖 BOT BASIC INFORMATION
# =========================================================
API_ID = int(environ.get("API_ID", "0"))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
PORT = int(environ.get("PORT", "8080"))
TIMEZONE = environ.get("TIMEZONE", "Asia/Kolkata")
OWNER_USERNAME = environ.get("OWNER_USERNAME", "RishuBotz_Bot")

# =========================================================
# 💾 DATABASE CONFIGURATION
# =========================================================
DB_URL = environ.get("DATABASE_URI", "")
DB_NAME = environ.get("DATABASE_NAME", "testing")

# =========================================================
# 📢 CHANNELS & ADMINS
# =========================================================
ADMINS = int(environ.get("ADMINS", "6286894502"))

LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002935300495"))
PREMIUM_LOGS = int(environ.get("PREMIUM_LOGS", "-1002935300495"))
VERIFIED_LOG = int(environ.get("VERIFIED_LOG", "-1002935300495"))

POST_CHANNEL = int(environ.get("POST_CHANNEL", "-1002935300495"))
VIDEO_CHANNEL = int(environ.get("VIDEO_CHANNEL", "-1003438674780"))
BRAZZER_CHANNEL = int(environ.get("BRAZZER_CHANNEL", "-1003428737875"))

# Auth channels list
auth_channel_str = environ.get("AUTH_CHANNEL", "-1003001351178")
AUTH_CHANNEL = [int(x) for x in auth_channel_str.split() if x.strip().lstrip("-").isdigit()]

# =========================================================
# ⚙️ FEATURES & TOGGLES  (FIXED)
# =========================================================
FSUB = str_to_bool(environ.get("FSUB"), True)
IS_VERIFY = str_to_bool(environ.get("IS_VERIFY"), False)
POST_SHORTLINK = str_to_bool(environ.get("POST_SHORTLINK"), False)
SEND_POST = str_to_bool(environ.get("SEND_POST"), False)

# =========================================================
# 🔢 LIMITS
# =========================================================
DAILY_LIMIT = int(environ.get("DAILY_LIMIT", "2"))
VERIFICATION_DAILY_LIMIT = int(environ.get("VERIFICATION_DAILY_LIMIT", "10"))
PREMIUM_DAILY_LIMIT = int(environ.get("PREMIUM_DAILY_LIMIT", "30"))

# =========================================================
# 🔗 SHORTLINK & VERIFICATION
# =========================================================
SHORTLINK_URL = environ.get("SHORTLINK_URL", "")
SHORTLINK_API = environ.get("SHORTLINK_API", "")
POST_SHORTLINK_URL = environ.get("POST_SHORTLINK_URL", "")
POST_SHORTLINK_API = environ.get("POST_SHORTLINK_API", "")
VERIFY_EXPIRE = int(environ.get("VERIFY_EXPIRE", "3600"))
TUTORIAL_LINK = environ.get("TUTORIAL_LINK", "")

# =========================================================
# 💳 PAYMENT SETTINGS
# =========================================================
UPI_ID = environ.get("UPI_ID", "@fam")
QR_CODE_IMAGE = environ.get("QR_CODE_IMAGE", "https://graph.org/file/cd8a38a7faf563e66fd99-9b0d740742deeaa30a.jpg")

# =========================================================
# 🖼️ IMAGES
# =========================================================
START_PIC = environ.get("START_PIC", "https://graph.org/file/d54d1586eb2f4a4e5d1ad-2c9b97e9c711a72bea.jpg")
AUTH_PICS = environ.get("AUTH_PICS", "https://graph.org/file/35f48240154fba008389a-92a97d0ffdeeaf3b0d.jpg")
VERIFY_IMG = environ.get("VERIFY_IMG", "https://graph.org/file/fef31a5b22070ac83eb40-46237caa18803737e1.jpg")
NO_IMG = environ.get("NO_IMG", "https://graph.org/file/fef31a5b22070ac83eb40-46237caa18803737e1.jpg")

# =========================================================
# 🌐 WEB APP
# =========================================================
WEB_APP_URL = environ.get("WEB_APP_URL", "")
