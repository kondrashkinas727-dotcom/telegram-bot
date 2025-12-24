import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
SESSIONS_DIR = "sessions"
FILES_DIR = "files"
os.makedirs(SESSIONS_DIR, exist_ok=True)
os.makedirs(FILES_DIR, exist_ok=True)
