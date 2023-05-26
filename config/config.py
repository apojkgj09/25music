import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
HEROKU_API_KEY = getenv("HEROKU_API_KEY") 
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/its-star-boi/ShizukaXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GITHUB_REPO = getenv("GITHUB_REPO", "https://github.com/its-star-boi/ShizukaXMusic")
GIT_TOKEN = getenv("GIT_TOKEN", None)

CHANNEL = getenv(
    "CHANNEL", "KB_HE"
)  # قناه الاشتراك الاجباري مثل هيك https://t.me/M_O_D_Y_CH
CHANNEL_SUDO = getenv(
    "CHANNEL_SUDO", "https://t.me/KB_HE"
)  # قناة السورس هيك https://t.me/M_O_D_Y_CH
SUPPORT_CHANNEL = getenv(
    "SUPPORT_CHANNEL", "https://t.me/KB_HE"
)  #جروب السورس https://t.me/BarGohara
SUPPORT_GROUP = getenv(
    "SUPPORT_GROUP", "https://t.me/FH_KP"
) 

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True")
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "5400"))
AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))
AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)
YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/343e5269a0d64c31f60b1.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/343e5269a0d64c31f60b1.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/35e6eebd266116eb258b8.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/f99216afa7794c1cfe880.jpg"

STATS_IMG_URL = "https://graph.org/file/a495d9428f83bbe7f31b4.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/f99216afa7794c1cfe880.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/a495d9428f83bbe7f31b4.jpg"

STREAM_IMG_URL = "https://graph.org/file/f99216afa7794c1cfe880.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/a495d9428f83bbe7f31b4.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/35e6eebd266116eb258b8.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/f99216afa7794c1cfe880.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/a495d9428f83bbe7f31b4.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/35e6eebd266116eb258b8.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/56d1760224589ee370186.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://te.legra.ph/file/56d1760224589ee370186.jpg"
