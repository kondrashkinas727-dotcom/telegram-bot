import os
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from config import API_ID, API_HASH, SESSIONS_DIR

class TelegramSessionManager:
    def __init__(self, user_id):
        self.user_id = user_id
        self.session_path = os.path.join(SESSIONS_DIR, f"user_{user_id}")
        self.client = TelegramClient(self.session_path, API_ID, API_HASH)

    async def connect(self):
        await self.client.connect()
        return self.client

    async def is_authorized(self):
        return await self.client.is_user_authorized()

    async def send_code(self, phone):
        await self.client.send_code_request(phone)

    async def sign_in(self, phone, code):
        try:
            await self.client.sign_in(phone=phone, code=code)
        except SessionPasswordNeededError:
            return "2FA"

    async def sign_in_password(self, password):
        await self.client.sign_in(password=password)
