from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "28768514"))
API_HASH = getenv("API_HASH", "40761fd256d71926ac455e55fcb71ae1")

BOT_TOKEN = getenv("BOT_TOKEN", "6757828951:AAGlDBUC3Dtq_ByKh0K6k-T-sNyWOPnyCYA")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "6634423600"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgG2-QIAHwh9cL2kectPPgIU57z0vHpYWQFSlq-CsO_DBbrrnuZ6MM_zH7d7mEU5qFzNpFcZyT3NT0Zy4lcG8uI63iUyqKdMmSe3_I8b7Yv4MeLJs_-ZMJW-xNS9f0QZioe8nruwqEWiFm80tb3JY9q9UVWQwFfkvxZYvMD6Twgj5vq5z3VPxPqSQ-WwchUSkiAcUN2rtkZuYimeOT-KCdqAWv22AdKw2eVHunFshMEgjBHtAgFvLhhhUaTr-VUB8u0wSMmjqEh848xR0YIbpdpMdY9TQIM91_h_SUkgVwLahlWg86JP4LupFckgVSI2x0U4Oc9S5ERz3kbOZ9EKFM8KpZwQAAAAF2FQicAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6634423600").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
