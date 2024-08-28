from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


start_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📃 Регистрация")],
    [KeyboardButton(text="🎫 Инфо")]
], resize_keyboard=True)


keyboard_if_user_validate = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="➕ LUCOIN")
    ],
    [
        KeyboardButton(text="🎫 Инфо"),
        KeyboardButton(text="💠 Профиль")
    ],
    [
        KeyboardButton(text='💊 Магазин', url='https://ru.lukoil-shop.com/'),
        KeyboardButton(text='🏆 Лидерборд')
    ]
], resize_keyboard=True)


stacking = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Открыть вклад', callback_data='open_stacking')],
    [InlineKeyboardButton(text='Проверить вклад', callback_data='check_balance_stake')]
], resize_keyboard=True)


shop_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="💵 Вклад")],
    [
        KeyboardButton(text="Смена имени"),
        KeyboardButton(text="Мерч", url='https://ru.lukoil-shop.com/'),
        KeyboardButton(text="⏪")
    ]
], resize_keyboard=True)


# yuraban = ReplyKeyboardMarkup(keyboard=[
#     [KeyboardButton(text='ИЗВИНИТЕ МЕНЯ, Я БОЛЬШЕ ТАК НЕ БУДУ')]
# ], resize_keyboard=True)


profile_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Перевод")],
    [KeyboardButton(text="⏪")]
], resize_keyboard=True)


transaction_keyboard = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Номер моего кошелька"),
        KeyboardButton(text="Перевести"),
        KeyboardButton(text="⏪")
    ]
], resize_keyboard=True)


shop_luk = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='открыть', url='https://ru.lukoil-shop.com/')],
], resize_keyboard=True)
