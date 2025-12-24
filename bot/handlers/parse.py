from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states import ParseState
from core.telegram_core import TelegramSessionManager
from core.parser_core import TelegramUserParser
from core.exporter import export_json

router = Router()

@router.message(commands=["parse"])
async def parse_start(message: Message, state: FSMContext):
    await state.set_state(ParseState.chat)
    await message.answer("Отправьте ссылку или @username чата:")

@router.message(ParseState.chat)
async def parse_chat(message: Message, state: FSMContext):
    session = TelegramSessionManager(message.from_user.id)
    client = await session.connect()
    if not await session.is_authorized():
        await message.answer("Сначала выполните /auth")
        return
    parser = TelegramUserParser(client)
    data = await parser.parse_users(message.text)
    file_path = export_json(data, f"users_{message.from_user.id}")
    await message.answer_document(document=open(file_path, "rb"))
    await state.clear()
