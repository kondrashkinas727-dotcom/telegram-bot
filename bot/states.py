from aiogram.fsm.state import StatesGroup, State

class AuthState(StatesGroup):
    phone = State()
    code = State()
    password = State()

class ParseState(StatesGroup):
    chat = State()
