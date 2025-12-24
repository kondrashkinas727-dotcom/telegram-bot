# -*- coding: utf-8 -*-

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.keyboards.inline import lang_keyboard, main_menu
from bot.states.fsm import LangState

router = Router()
user_lang = {}

@router.message(CommandStart())
async def start_cmd(message: Message, state: FSMContext):
    await state.set_state(LangState.choosing_lang)
    await message.answer("Choose language / Выберите язык:", reply_markup=lang_keyboard())

@router.callback_query(F.data.startswith("lang_"))
async def set_lang(call: CallbackQuery, state: FSMContext):
    lang = call.data.split("_")[1]
    user_lang[call.from_user.id] = lang
    await state.clear()

    text = "Язык установлен" if lang == "ru" else "Language set"
    await call.message.answer(text, reply_markup=main_menu(lang))
    await call.answer()
