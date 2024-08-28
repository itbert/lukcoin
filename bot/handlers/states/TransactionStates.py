from aiogram.fsm.state import StatesGroup, State


class Transaction(StatesGroup):
    user_wallet = State()
    transaction_amount = State()
