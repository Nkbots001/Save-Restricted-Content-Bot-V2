# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "22808125"))
API_HASH = getenv("API_HASH", "406c09543fec722fe3c48ca2f06d78de")
BOT_TOKEN = getenv("BOT_TOKEN", "6382878040:AAHCt6-8jE740iHrfaOJ7_L6WH-vx2h4hqI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "819861991").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://Nkbot001:nkbot123@cluster0.5crfy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1001916142483")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001988879902"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
