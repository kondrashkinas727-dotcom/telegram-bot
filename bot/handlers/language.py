# -*- coding: utf-8 -*-

from aiogram import Router
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart

router = Router()

user_lang = {}


def main_menu(lang: str) -> str:
    if lang == "ru":
        return (
            "Главное меню:\n\n"
            "/auth — авторизация\n"
            "/parse — парсинг чатов и каналов"
        )
    return (
        "Main menu:\n\n"
        "/auth — authorization\n"
        "/parse — chat and channel parsing"
    )


@router.message(CommandStart())
async def start_lang(message: Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru"),
                InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en"),
            ]
        ]
    )
    await message.answer("Choose language / Выберите язык:", reply_markup=kb)


@router.callback_query(lambda c: c.data.startswith("lang_"))
async def set_language(callback):
    lang = callback.data.split("_")[1]
    user_lang[callback.from_user.id] = lang

    if lang == "ru":
        text = "Язык установлен: Русский\n\n" + main_menu("ru")
    else:
        text = "Language set: English\n\n" + main_menu("en")

    await callback.message.answer(text)
    await callback.answer()
