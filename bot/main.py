# -*- coding: utf-8 -*-

import asyncio
import os

from aiogram import Bot, Dispatcher
from fastapi import FastAPI
import uvicorn

from config import BOT_TOKEN
from bot.handlers import start, language, auth, parse
from core.db import init_db

# ---------- HTTP APP ----------
app = FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}

# ---------- TELEGRAM BOT ----------
async def start_bot():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start.router)
    dp.include_router(language.router)
    dp.include_router(auth.router)
    dp.include_router(parse.router)

    await dp.start_polling(bot)

# ---------- MAIN ----------
async def main():
    init_db()

    port = int(os.environ.get("PORT", 10000))

    await asyncio.gather(
        start_bot(),
        uvicorn.Server(
            uvicorn.Config(
                app,
                host="0.0.0.0",
                port=port,
                log_level="info"
            )
        ).serve()
    )

if __name__ == "__main__":
    asyncio.run(main())
