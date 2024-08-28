# from aiogram import Bot, Dispatcher, types, Router, F
# from aiogram.filters import CommandStart, Command
# import asyncio
# from aiogram.fsm.state import StatesGroup, State
# from aiogram.fsm.context import FSMContext
# from data_base import db
# API_TOKEN = '7005640058:AAF-3prmH5KYxMarKmcPhjIjM1Z2gmwBQHQ'
# bot = Bot(token=API_TOKEN)
# dp = Dispatcher()
# router = Router()
# dp.include_router(router)
# from time import time
# interval = 10
#
# class form(StatesGroup):
#     name = State()
#     age = State()
#
#
# @router.message(Command('start'))
# async def start_profile(message: types.Message,state: FSMContext):
#     db.update({message.from_user.id:dict({'coins':0, 'last_farm':0})})
#     await state.set_state((form.name))
#     await message.answer('введите имя')
#
#
# @router.message(form.name)
# async def form_name(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     nm = message.text
#     db[message.from_user.id].update({'name':nm})
#     await state.set_state(form.age)
#     await message.answer('теперь возраст')
#     print(form.name)
#
#
# @router.message(form.age)
# async def form_age(message: types.Message, state: FSMContext):
#     ager = int(message.text)
#     if ager < 16:
#         await message.answer('извините, но пользоватьс нашим приложенгием можно только с 16 лет')
#         await state.clear()
#     await state.update_data(age=message.text)
#     ag = message.text
#     db[message.from_user.id].update({'age':ag})
#     await message.answer('Отлично, тьперь вы можете приступить к сбору ЛУкоинов')
#     print(db)
#     await state.clear()
#
#
#
#
# @router.message(Command('getcoins'))
# async def form_age(message: types.Message, state: FSMContext):
#     cur_time = time()
#     if cur_time-db[message.from_user.id]['last_farm']>10:
#         db[message.from_user.id].update({'coins': db[message.from_user.id]['coins']+10})
#         db[message.from_user.id].update({'last_farm': cur_time})
#         await message.reply('вам начислено 10 lucoin-ов')
#     else:
#         await message.reply(f"подождите ещё {   round(10-(cur_time-db[message.from_user.id]['last_farm']),1)} секунд")
#     print(db)
#
#
#
# # @router.message(lambda message: message.text == "зарегаться")
# # async def send_hi(message: types.Message):
# #     await message.answer("hi")
#
#
# async def main():
#     await dp.start_polling(bot)
#
#
# if __name__ == '__main__':
#     asyncio.run(main())
