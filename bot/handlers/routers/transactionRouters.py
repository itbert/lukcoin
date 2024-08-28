from aiogram import F, Router
from aiogram.fsm.context import FSMContext

from bot.keyboards.keyboardsMainPage import *
from bot.handlers.states.TransactionStates import Transaction

from database.pseudo_database.db import db
from database.pseudo_database.db import transactions_base


router_transaction = Router()


@router_transaction.message(F.text == "Перевод")
async def translate(message: Message, state: FSMContext):
    await message.answer('⏬ Введите номер кошелька, на который желаете перевести коины ⏬')
    await state.set_state(Transaction.user_wallet)


@router_transaction.message(Transaction.user_wallet)
async def tr2(message: Message, state: FSMContext):

    recipient_id = int(message.text)
    donor_id = message.from_user.id
    transactions_base.update({donor_id: recipient_id})

    await state.update_data(user_wallet=recipient_id)

    await message.answer('Введите количество LUKCOIN-ов для перевода')

    await state.set_state(Transaction.transaction_amount)


@router_transaction.message(Transaction.transaction_amount)
async def tr3(message: Message, state: FSMContext):

    transaction_amount = int(message.text)
    donor_id = message.from_user.id

    if 15 <= transaction_amount < db[donor_id]['coins']:

        await state.update_data(transaction_amount=transaction_amount)

        db[donor_id]['coins'] -= transaction_amount
        db[transactions_base[donor_id]]['coins'] += transaction_amount

        # print(db)

        await message.answer(
            text=f'✔ ПЕРЕВОД ПО НОМЕРУ КОШЕЛЬКА ✔\n'
                 f'\n🍃 Отправитель: {db[donor_id]["name"]}'
                 f'\n🎁 Получатель: {db[transactions_base[donor_id]]["name"]}'
                 f'\n💰 Сумма перевода {transaction_amount} коинов'
        )

        """
        TODO: Написать отправку сообщений в чат пользователю с переводом
        """

        transactions_base.pop(donor_id)

        # print(transactions_base)

        await state.clear()
    else:
        await message.answer('💲 На вашем счете недостаточно средств для совершения перевода')
        await state.clear()
