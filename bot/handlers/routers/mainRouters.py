from time import time

from aiogram import F, Router
from aiogram.fsm.context import FSMContext

from bot.handlers.states.MainStates import SetNewName
from bot.keyboards.keyboardsMainPage import *

from database.pseudo_database.db import db


router = Router()


# Фарм коинов
@router.message(F.text == "➕ LUCOIN")
async def form_age(message: Message):

    # Получение данных о времени и пользователе
    cur_time: float = time()
    ID: id = message.from_user.id

    # Проверка на возраст, фарм коинов
    if db[ID]['age'] >= 16:
        if cur_time - db[message.from_user.id]['last_farm'] > 18000:

            db[ID].update({
                'coins': db[ID]['coins'] + 50  # + 10_000 если тестим/показываем
            })

            db[ID].update({'last_farm': cur_time})

            await message.reply('+ 50 LUKCOIN-ов')
        else:
            await message.reply(f"Подождите {round((18000 - (cur_time - db[ID]['last_farm'])) / 60)} минут "
                                f"до следующего фарма")

        # print(db)

    else:
        await message.answer(text='💢 Вам должно быть больше 16 лет чтобы фармить')


@router.message(F.text == "💠 Профиль")
async def show_data(message: Message):

    ID: int = message.from_user.id

    # Получение данных о пользователе

    name: str = db[ID]['name']
    coins: int = db[ID]['coins']
    wallet: int = ID

    await message.answer(
        text=f"🗿 Пользователь: {name}"
             f"\n💎 LUCOIN-ов: {coins}"
             f"\n🌯 Номер кошелька: {wallet}",
        reply_markup=profile_keyboard
    )


@router.message(F.text == '💊 Магазин')
async def go_to_shop(message: Message):
    await message.answer(
        text='Выберите действие',
        reply_markup=shop_keyboard
    )


@router.message(F.text == '💵 Вклад')
async def go_to_stake_my_money(message: Message):
    await message.answer(
        text='Выберите действие',
        reply_markup=stacking
    )


@router.message(F.text == '⏪')
async def back_to_menu(message:  Message, state: FSMContext):
    await message.answer(
        text='Главное меню',
        reply_markup=keyboard_if_user_validate
    )

    await state.clear()


@router.message(F.text == 'Смена имени')
async def start_change_name(message:  Message, state: FSMContext):

    ID: int = message.from_user.id

    # Списание коинов за операцию

    if int(db[ID]['coins']) >= 5:
        await message.answer('Введите новое имя')
        db[ID]['coins'] -= 150
        await state.set_state(SetNewName.new_name)
    else:
        await message.answer(f'Недостатончо LUKCOIN-ов \n'
                             f'Стоимость смены имени: 150\n'
                             f'У вас: {db[ID]["coins"]}')

        await state.clear()


@router.message(SetNewName.new_name)
async def change_name(message: Message, state: FSMContext):

    ID: int = message.from_user.id
    new_username: str = message.text

    # Сбор данных (выше)
    # Изменение имени на новое

    await state.update_data(new_name=new_username)

    db[ID]['name'] = new_username

    await message.answer(f'Имя изменено на {new_username}'
                         f'\nСписано 150 LUKCOIN-ов')

    # print(db) - для проверки изменения имени пользователя

    await state.clear()


@router.message(F.text == '🏆 Лидерборд')
async def leader_bord(message:  Message):

    users: dict = db.keys()

    user_table: list = [(
        userid,
        db[userid]['coins'],
        db[userid]['name']) for userid in users
    ]
    # Сортировка списка пользователей по количеству коинов

    user_table.sort(key=lambda x: int(x[1]))

    # print(user_table)

    await message.answer(text=f'📊 Таблица лидеров'
                              f'\n1️⃣ {db[user_table[-1][0]]["name"]} - {db[user_table[-1][0]]["coins"]}'
                              f'\n2️⃣ {db[user_table[-2][0]]["name"]} - {db[user_table[-2][0]]["coins"]}'
                              f'\n3️⃣ {db[user_table[-3][0]]["name"]} - {db[user_table[-3][0]]["coins"]}')


@router.message(F.text == 'Мерч')
async def shop(message: Message):
    await message.answer(
        text='Магазин ЛУКОЙЛа любимого ❤',
        reply_markup=shop_luk
    )
