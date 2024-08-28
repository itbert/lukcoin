import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.handlers.routers.mainRouters import router
from bot.handlers.routers.startRouters import router_start
from bot.handlers.routers.stackingRouters import router_stake
from bot.handlers.routers.transactionRouters import router_transaction

from resources.secret_data.config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(router_start, router, router_stake, router_transaction)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # ТОЛЬКО ПРИ ДЕБАГЕ
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit !')
