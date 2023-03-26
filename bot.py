import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from tgbot.config import load_config
from tgbot.middlewares.config import ConfigMiddleware
from tgbot.services import broadcaster
from tgbot import handlers
from tgbot.misc.commands import set_commands

logger = logging.getLogger(__name__)

config = load_config(".env")
storage = MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
dp = Dispatcher(storage=storage)


async def on_startup(bot: Bot, admin_ids: list[int]):
    await set_commands(bot)
    await broadcaster.broadcast(bot, admin_ids, "Бот був запущений")


def register_global_middlewares(dp: Dispatcher, config):
    dp.message.outer_middleware(ConfigMiddleware(config))
    dp.callback_query.outer_middleware(ConfigMiddleware(config))


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    dp.include_router(handlers.router)

    register_global_middlewares(dp, config)

    await on_startup(bot, config.tg_bot.admin_ids)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Бот був вимкнений!")
