from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(
            command='start',
            description='Старт'
        ),
        BotCommand(
            command='save_address',
            description='Зберегти адресу'
        ),
        BotCommand(
            command='svitlo',
            description='Інформація про відключення'
        ),
        BotCommand(
            command='help',
            description='допомога'
        )
    ]
    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())
