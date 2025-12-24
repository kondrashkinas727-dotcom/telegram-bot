from aiogram import Router
from aiogram.types import Message

router = Router()

@router.message()
async def start(message: Message):
    await message.answer("?? Привет!\n/auth - авторизация\n/parse - парсинг")
