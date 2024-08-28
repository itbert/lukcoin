from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboardsMainPage import *
from bot.handlers.states.StartState import RegForm

from database.pseudo_database.db import *


router_start = Router()


@router_start.message(CommandStart())
async def start_command(message: Message):
    # userok = message.from_user.id
    # if userok == 5288849370 or userok == 1023964787:
    #     await message.answer('ЮРА ТЫ ЗАБАНЕН', reply_markup=yuraban)
    # else:
        if message.from_user.id not in users:
            await message.answer(
                text='Похоже, что вы новый пользователь, приветствуем '
                     '\nНачните прямо сейчас! '
                     '\nВыберите одну из доступных команд.',
                reply_markup=start_keyboard
            )
            db.update({
                message.from_user.id: dict({
                    'coins': 0,
                    'last_farm': 0
                })
            })
        else:
            await message.reply(
                text=f'С возвращением, {message.from_user.first_name}!',
                reply_markup=keyboard_if_user_validate)


# @router_start.message(F.text == 'ИЗВИНИТЕ МЕНЯ, Я БОЛЬШЕ ТАК НЕ БУДУ')
# async def sorry(message: Message):
#     await message.answer('Ладно, Юра, но больше не спамь')
#     if message.from_user.id not in users:
#         await message.answer(text='Добрый день, похоже, что вы новый пользователь это бот <<бот>>, '
#                                   '<<приветственный тескт>>',
#                              reply_markup=start_keyboard)
#         db.update({
#             message.from_user.id: dict({
#                 'coins': 0,
#                 'last_farm': 0
#             })
#         })
#     else:
#         await message.reply(
#             text=f'с возвращением, {message.from_user.first_name}',
#             reply_markup=keyboard_if_user_validate)


@router_start.message(F.text == "📃 Регистрация")
async def register(message: Message, state: FSMContext):
    await message.answer(text="Введите ваше имя")
    await state.set_state(RegForm.username)


@router_start.message(F.text == "🎫 Инфо")
async def help_text(message: Message):
    await message.answer(
        text="С чего начать?"
             "\nФармить коины! Это основное, чем вам "
             "придется заниматься. Так же вы можете открыть "
             "вклад и зарабатывать коины активнее"
    )


@router_start.message(RegForm.username)
async def form_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    name_user = message.text
    # if name_user == 'Юра':
    #     await message.answer(f'Тебе нельзя же ну', reply_markup=yuraban)
    # else:
    #     pass
    ID = message.from_user.id
    db[ID].update({'name': name_user})
    await message.answer(text='Введите возраст')
    await state.set_state(RegForm.userage)


@router_start.message(RegForm.userage)
async def form_age(message: Message, state: FSMContext):
    ager = int(message.text)
    if ager < 16 or ager > 80:
        await state.update_data(age=message.text)
        ag = int(message.text)
        db[message.from_user.id].update({'age': ag})
        await message.answer(text='Пользоваться нашим ботом можно с 16 лет')
        await state.clear()

    else:
        await state.update_data(age=message.text)
        age = int(message.text)
        db[message.from_user.id].update({'age': age})
        await message.answer(
            text='Отлично, теперь вы можете приступить к сбору LUKCOIN',
            reply_markup=keyboard_if_user_validate
        )
        await state.clear()
