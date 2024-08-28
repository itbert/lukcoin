from aiogram.fsm.state import State, StatesGroup


class SetNewName(StatesGroup):
    new_name = State()


class StakingStates(StatesGroup):
    waiting_for_amount = State()
    waiting_for_period = State()
