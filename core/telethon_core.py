from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from config import API_ID, API_HASH
import os

SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

def get_client(user_id: int):
    return TelegramClient(
        f"{SESSIONS_DIR}/{user_id}",
        API_ID,
        API_HASH
    )
