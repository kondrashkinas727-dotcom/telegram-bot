from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def lang_keyboard():
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🇷🇺 Русский", callback_data="lang_ru")],
        [InlineKeyboardButton(text="🇬🇧 English", callback_data="lang_en")]
    ])


def main_menu(lang: str):
    if lang == "ru":
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🔐 Авторизация", callback_data="auth")],
            [InlineKeyboardButton(text="📊 Парсинг", callback_data="parse")]
        ])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔐 Authorization", callback_data="auth")],
        [InlineKeyboardButton(text="📊 Parsing", callback_data="parse")]
    ])


def parse_type_kb(lang: str):
    if lang == "ru":
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="💬 Чат", callback_data="chat")],
            [InlineKeyboardButton(text="📢 Канал", callback_data="channel")]
        ])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="💬 Chat", callback_data="chat")],
        [InlineKeyboardButton(text="📢 Channel", callback_data="channel")]
    ])


def access_kb(lang: str):
    if lang == "ru":
        return InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="🌐 Открытый", callback_data="public")],
            [InlineKeyboardButton(text="🔒 Приватный", callback_data="private")]
        ])
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🌐 Public", callback_data="public")],
        [InlineKeyboardButton(text="🔒 Private", callback_data="private")]
    ])
