from telethon import TelegramClient
from config import API_ID, API_HASH
import os

SESSIONS_DIR = "sessions"
os.makedirs(SESSIONS_DIR, exist_ok=True)

# 🔑 ГЛОБАЛЬНЫЙ КЭШ КЛИЕНТОВ
_clients: dict[int, TelegramClient] = {}


def get_client(user_id: int) -> TelegramClient:
    if user_id not in _clients:
        _clients[user_id] = TelegramClient(
            session=f"{SESSIONS_DIR}/{user_id}",
            api_id=API_ID,
            api_hash=API_HASH
        )
    return _clients[user_id]
