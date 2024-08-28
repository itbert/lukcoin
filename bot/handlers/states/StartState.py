from aiogram.fsm.state import StatesGroup, State


class RegForm(StatesGroup):
    username = State()
    userage = State()
