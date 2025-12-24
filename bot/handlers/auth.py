# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("auth"))
async def auth_cmd(message: Message):
    await message.answer("Авторизация будет добавлена позже.")
