# -*- coding: utf-8 -*-

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from telethon.errors import SessionPasswordNeededError

from bot.states.fsm import AuthState
from bot.handlers.start import user_lang
from core.telethon_core import get_client

router = Router()


@router.callback_query(F.data == "auth")
async def auth_start(call: CallbackQuery, state: FSMContext):
    lang = user_lang.get(call.from_user.id, "ru")
    text = "Введите номер телефона:" if lang == "ru" else "Enter phone number:"
    await state.set_state(AuthState.phone)
    await call.message.answer(text)
    await call.answer()


@router.message(AuthState.phone)
async def auth_phone(message: Message, state: FSMContext):
    client = get_client(message.from_user.id)
    await client.connect()

    phone = message.text.strip()
    await client.send_code_request(phone)

    await state.update_data(phone=phone)
    await state.set_state(AuthState.code)
    await message.answer("Введите код из Telegram:")


@router.message(AuthState.code)
async def auth_code(message: Message, state: FSMContext):
    data = await state.get_data()
    client = get_client(message.from_user.id)

    code = message.text.strip().replace(" ", "")

    try:
        await client.sign_in(phone=data["phone"], code=code)

        if await client.is_user_authorized():
            await message.answer("✅ Авторизация успешна")
            await state.clear()
        else:
            await message.answer("❌ Не удалось авторизоваться")
            await state.clear()

    except SessionPasswordNeededError:
        await state.set_state(AuthState.password)
        await message.answer("🔐 Введите пароль 2FA:")

    except Exception as e:
        await message.answer(f"❌ Ошибка авторизации:\n{e}")
        await state.clear()


@router.message(AuthState.password)
async def auth_password(message: Message, state: FSMContext):
    client = get_client(message.from_user.id)
    password = message.text.strip()

    try:
        await client.sign_in(password=password)

        if await client.is_user_authorized():
            await message.answer("✅ Авторизация успешна (2FA)")
        else:
            await message.answer("❌ Ошибка 2FA")

    except Exception as e:
        await message.answer(f"❌ Ошибка 2FA:\n{e}")

    await state.clear()
