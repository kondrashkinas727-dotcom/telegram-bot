from aiogram.fsm.state import State, StatesGroup


class LangState(StatesGroup):
    choosing_lang = State()


class AuthState(StatesGroup):
    phone = State()
    code = State()
    password = State()


class ParseState(StatesGroup):
    choose_type = State()
    choose_access = State()
    link = State()
