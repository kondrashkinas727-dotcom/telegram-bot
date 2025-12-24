# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from bot.state import user_languages

router = Router()

@router.message(Command("ru"))
async def set_ru(message: Message):
    user_languages[message.from_user.id] = "ru"
    await message.answer("Язык установлен: Русский")

@router.message(Command("en"))
async def set_en(message: Message):
    user_languages[message.from_user.id] = "en"
    await message.answer("Language set: English")