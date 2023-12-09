import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    # BOT_TOKEN = os.environ.get("BOT_TOKEN", "6100891233:AAHo_OjnFWTdY_JewRdcqphxASAcAK1IHVg") #ajhhsa
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5872747581:AAH7_XPCOCEVfbgUhepjJWlcOmj8wjDTjBk") #jn_url

    API_ID = int(os.environ.get("API_ID", "3393749"))

    API_HASH = os.environ.get("API_HASH", "a15a5954a1db54952eebd08ea6c68b71")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "1061576483").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATES_CHANNEL = os.environ.get("UPDATE_CHANNEL", "-1001512853438")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @url_uploaderV3Bott"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Jayanna:Jayanna2023@yash.tm1c2bd.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "TG_FILES")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001512853438"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "1061576483"))
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "dgfghgjbot")

    PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "1061576483").split()))

    PRO_USERS.append(OWNER_ID)
