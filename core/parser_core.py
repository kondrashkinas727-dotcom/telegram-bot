from telethon.tl.types import User
from datetime import datetime

class TelegramUserParser:
    def __init__(self, client):
        self.client = client

    async def parse_users(self, chat):
        users = {}
        async for message in self.client.iter_messages(chat):
            sender = await message.get_sender()
            if isinstance(sender, User) and sender.id not in users:
                users[sender.id] = {
                    "user_id": sender.id,
                    "username": sender.username,
                    "first_name": sender.first_name,
                    "last_name": sender.last_name
                }

        return {
            "chat": str(chat),
            "parsed_at": datetime.utcnow().isoformat(),
            "total_users": len(users),
            "users": list(users.values())
        }
