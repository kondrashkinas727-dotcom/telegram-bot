import asyncio
from core.db import init_db
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from bot.handlers import start, auth, parse

async def main():
    init_db()
    bot = Bot(token=BOT_TOKEN)
    dp.include_router(start.router)
    dp.include_router(auth.router)
    dp.include_router(parse.router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
