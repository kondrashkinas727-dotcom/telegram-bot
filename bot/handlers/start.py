# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Привет!\n\n"
        "/auth — авторизация\n"
        "/parse — парсинг чатов и каналов"
    )
