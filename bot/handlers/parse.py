# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("parse"))
async def parse_cmd(message: Message):
    await message.answer("Парсер в разработке.")
