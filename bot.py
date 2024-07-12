import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage, Redis
from aiogram.fsm.storage.memory import MemoryStorage

from config_data.config import Config, load_config
from db.db_id import create_database
from handlers import tax_and_lawer_handlers, education_handlers, loan_handlers, \
    finance_start_handlers, account_handlers, register_handlers, \
    finance_active_handlers, finance_common_handlers, about_us_handlers
from keyboards.main_menu import set_main_menu


async def main() -> None:
    config: Config = load_config()
    bot: Bot = Bot(config.tg_bot.token, parse_mode="HTML")
    await create_database()
    storage = MemoryStorage()
    dp: Dispatcher = Dispatcher(storage=storage)

    # Настраиваем главное меню бота
    await set_main_menu(bot)

    # Регистриуем роутеры в диспетчере
    dp.include_router(finance_common_handlers.router)
    dp.include_router(tax_and_lawer_handlers.router)
    dp.include_router(education_handlers.router)
    dp.include_router(loan_handlers.router)
    dp.include_router(finance_start_handlers.router)
    dp.include_router(account_handlers.router)
    #dp.include_router(register_handlers.router)
    dp.include_router(finance_active_handlers.router)
    dp.include_router(about_us_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
