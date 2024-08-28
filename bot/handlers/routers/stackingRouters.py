from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from datetime import datetime

from bot.keyboards.keyboardsMainPage import *
from bot.handlers.states.MainStates import StakingStates

from database.pseudo_database.db import db


router_stake = Router()


@router_stake.callback_query(F.data == 'open_stacking')
async def stacking_one(message: Message, state: FSMContext):

    ID: int = message.from_user.id

    coins: int = db[ID]['coins']

    await message.answer(
        text=f"Выберите количество валюты для стейкинга, у вас: {coins}",
        show_alert=True
    )
    await state.set_state(StakingStates.waiting_for_amount)


@router_stake.message(StakingStates.waiting_for_amount)
async def stacking_two(message: Message, state: FSMContext):

    amount = int(message.text)
    ID: int = message.from_user.id

    coins: int = db[ID]['coins']

    # Достаточно ли монет для открытия вклада

    if 50 <= amount <= coins:

        await message.answer(text=f"Вы выбрали {amount} LUKCOIN-ов")

        t = datetime.now()
        time_start = t.day

        # Обновление словаря с вкладом

        db[ID].update({
            'stacking': {
                'amount_stacking': amount,
                'period_stacking': 0,
                'start_stacking': time_start,
                'end_stacking': 0
            }
        })

        # Списание за открытие вклада

        db[ID]['stacking']['amount_stacking'] = amount
        db[ID]['coins'] -= amount

        await message.answer(text=f'На вашем балансе осталось: {db[ID]["coins"]} LUKCOIN')
        await message.answer(text=f'Выберите период вклада (от 2-х до 10-и дней)')

        await state.set_state(StakingStates.waiting_for_period)

    else:
        await message.answer(text=f"Недостаточно средств, у вас: {db[ID]['coins']}. "
                                  f"\nМинимум для открытия вклада: 100 коинов")

        await state.set_state(StakingStates.waiting_for_amount)


@router_stake.message(StakingStates.waiting_for_period)
async def stacking_three(message: Message, state: FSMContext):

    ID: int = message.from_user.id

    period_of_stacking: int = int(message.text)

    if period_of_stacking < 2 or period_of_stacking > 10:
        await message.answer(
            text='💢 Вы выбрали неправильный период вклада!!'
                 '\nНо коины мы уже списали, сам(-а) виноват(-а)'
        )

        await state.clear()
    else:
        start_stacking: int = db[ID]['stacking']['start_stacking']

        db[ID]['stacking']['period_stacking'] = period_of_stacking
        db[ID]['stacking']['end_stacking'] = start_stacking + period_of_stacking

        await message.reply(text=f'Успешно! Период вклада {db[ID]["stacking"]["period_stacking"]} д.,'
                                 f'\nДеньги вернутся на вклад через {db[ID]["stacking"]["period_stacking"]} д.')

        await state.clear()


@router_stake.callback_query(F.data == 'check_balance_stake')
async def check_balance_of_stake(message: Message):

    ID: int = message.from_user.id

    amount = int(db[ID]['stacking']['amount_stacking'])
    period = int(db[ID]['stacking']['period_stacking'])

    expected_percent: float | int = period / 10 + 1
    profit = round(amount * expected_percent)

    await message.answer(
        text=f"🎈 Актуальный вклад на вашем аккаунте: "
             f"\nСумма вклада {amount}"
             f"\nПериод {period}"
             f"\nОжидаемо для получения {profit}",
        show_alert=True
    )

    today = datetime.now().day
    end = db[ID]['stacking']['end_stacking']

    coins: int = db[ID]['coins']

    if today == end:
        coins_after_stake = coins + profit
        await message.answer(
            text=f"Ваш вклад был пополнен!"
                 f"\nСумма на вкладе: {amount}"
                 f"\nИтого получено: {profit}"
                 f"\nОбщая сумма счёта: {coins_after_stake}",
            show_alert=True
        )
    else:
        await message.answer(
            text=f'Еще не время для снятия денег с вклада'
                 f'\nВернитесь {end} числа'
        )
