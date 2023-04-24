import asyncio
import logging
from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from src.config import load_config
from src.handlers.start import register_info
from src.handlers.currency import register_currency
from src.handlers.koteo import register_koteo
from src.handlers.weather import register_weather
from src.handlers.polls import register_poll



logger = logging.getLogger(__name__)

def register_handlers(dp):
    register_info(dp)
    register_currency(dp)
    register_koteo(dp)
    register_weather(dp)
    register_poll(dp)

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )

    logger.info('Starting Bot')
    config = load_config('.env')
    bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())

    bot['config'] = config

    register_handlers(dp)


    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")