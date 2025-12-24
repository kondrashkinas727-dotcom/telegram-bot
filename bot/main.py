# -*- coding: utf-8 -*-

import asyncio
from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from bot.handlers import start, language, auth, parse
from core.db import init_db   # 👈 ВАЖНО

async def main():
    # 1️⃣ Инициализация БД
    init_db()

    # 2️⃣ Бот и диспетчер
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    # 3️⃣ Роутеры
    dp.include_router(start.router)
    dp.include_router(language.router)
    dp.include_router(auth.router)
    dp.include_router(parse.router)

    # 4️⃣ Старт бота
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
