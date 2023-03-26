from tgbot.classes.automation import Automation
from aiogram import Router, Bot
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, BufferedInputFile

router = Router(name='get_info')


@router.message(Command(commands=['svitlo']))
async def user_svitlo(message: Message, command: CommandObject, bot: Bot):
    if command.args:
        try:
            await message.answer(f'Будь ласка, зачекайте...')
            address = [s.strip() for s in command.args.split(',')]
            automation = Automation(address[0], address[1])
            await message.answer(automation.text())
            await bot.send_photo(message.chat.id, BufferedInputFile(automation.image(), filename='image.png'))
        except Exception:
            await message.answer(f'Ой! Щось пішло не так. Будь ласка, перевірте правильність написання вулиці.'
                                 f'За допомогою оберіть команду /help')
