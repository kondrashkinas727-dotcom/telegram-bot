# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("start"))
async def start_cmd(message: Message):
    await message.answer(
        "Choose language:\n\n"
        "/ru — Русский\n"
        "/en — English"
    )