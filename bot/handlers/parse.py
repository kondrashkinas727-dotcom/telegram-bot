# -*- coding: utf-8 -*-

from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from telethon.errors import ChatAdminRequiredError, ChannelPrivateError

from bot.states.fsm import ParseState
from bot.handlers.start import user_lang
from core.telethon_core import get_client

router = Router()

@router.callback_query(F.data == "parse")
async def parse_start(call: CallbackQuery, state: FSMContext):
    lang = user_lang.get(call.from_user.id, "ru")
    from bot.keyboards.inline import parse_type_kb
    await state.set_state(ParseState.choose_type)
    await call.message.answer("Выберите тип:" if lang == "ru" else "Choose type:", reply_markup=parse_type_kb(lang))
    await call.answer()

@router.callback_query(ParseState.choose_type)
async def choose_type(call: CallbackQuery, state: FSMContext):
    await state.update_data(type=call.data)
    from bot.keyboards.inline import access_kb
    lang = user_lang.get(call.from_user.id, "ru")
    await state.set_state(ParseState.choose_access)
    await call.message.answer("Тип доступа:" if lang == "ru" else "Access type:", reply_markup=access_kb(lang))
    await call.answer()

@router.callback_query(ParseState.choose_access)
async def choose_access(call: CallbackQuery, state: FSMContext):
    await state.update_data(access=call.data)
    lang = user_lang.get(call.from_user.id, "ru")
    await state.set_state(ParseState.link)
    await call.message.answer("Отправьте ссылку:" if lang == "ru" else "Send link:")
    await call.answer()

@router.message(ParseState.link)
async def parse_link(message: Message, state: FSMContext):
    client = get_client(message.from_user.id)
    await client.connect()

    if not await client.is_user_authorized():
        await message.answer("❌ Сначала авторизуйтесь /auth")
        return

    try:
        entity = await client.get_entity(message.text)
        users = []

        async for user in client.iter_participants(entity):
            if user.username:
                users.append(f"@{user.username}")

        if not users:
            await message.answer(
                "❌ Участники скрыты или нет доступа.\n"
                "✔️ Проверьте подписку\n"
                "✔️ Проверьте, не скрыты ли участники"
            )
            return

        filename = f"parsed_{message.from_user.id}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(users))

        await message.answer(f"✅ Готово. Найдено: {len(users)}")

    except (ChatAdminRequiredError, ChannelPrivateError):
        await message.answer(
            "❌ Нет доступа.\n"
            "✔️ Проверьте, что вы участник\n"
            "✔️ Проверьте, что участники не скрыты"
        )

    await state.clear()
