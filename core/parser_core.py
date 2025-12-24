# -*- coding: utf-8 -*-

import os
from telethon.tl.types import User
from core.telethon_core import get_client

FILES_DIR = "files"
os.makedirs(FILES_DIR, exist_ok=True)


async def parse_participants(user_id: int, target: str) -> str:
    """
    Возвращает путь к файлу с username участников
    """

    client = get_client(user_id)
    await client.connect()

    entity = await client.get_entity(target)

    usernames = []

    async for user in client.iter_participants(entity):
        if isinstance(user, User) and user.username:
            usernames.append(f"@{user.username}")

    file_path = os.path.join(FILES_DIR, f"participants_{user_id}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
        for u in usernames:
            f.write(u + "\n")

    return file_path
