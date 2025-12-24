from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from bot.states import AuthState
from core.telegram_core import TelegramSessionManager

router = Router()

@router.message(commands=["auth"])
async def auth_start(message: Message, state: FSMContext):
    await state.set_state(AuthState.phone)
    await message.answer("Введите номер телефона:")

@router.message(AuthState.phone)
async def auth_phone(message: Message, state: FSMContext):
    await state.update_data(phone=message.text)
    session = TelegramSessionManager(message.from_user.id)
    await session.connect()
    await session.send_code(message.text)
    await state.set_state(AuthState.code)
    await message.answer("Введите код из Telegram:")

@router.message(AuthState.code)
async def auth_code(message: Message, state: FSMContext):
    data = await state.get_data()
    session = TelegramSessionManager(message.from_user.id)
    await session.connect()
    result = await session.sign_in(data["phone"], message.text)
    if result == "2FA":
        await state.set_state(AuthState.password)
        await message.answer("Введите пароль 2FA:")
    else:
        await state.clear()
        await message.answer("Авторизация успешна!")

@router.message(AuthState.password)
async def auth_password(message: Message, state: FSMContext):
    session = TelegramSessionManager(message.from_user.id)
    await session.connect()
    await session.sign_in_password(message.text)
    await state.clear()
    await message.answer("Авторизация завершена!")
