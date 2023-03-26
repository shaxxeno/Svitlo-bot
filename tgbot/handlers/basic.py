from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name='start_router')


@router.message(Command(commands=['start']))
async def user_start(message: Message):
    await message.answer(f'Привіт, {message.from_user.first_name}!'
                         f'\nЗа допомогою мене ти зможеш дізнатися, чи є світло у твоїй оселі!'
                         f'\n\n/help - допомога'
                         f'\n/save_address - зберегти адресу'
                         f'\n/svitlo - перевірити світло за вказаною адресою')


@router.message(Command(commands=['help']))
async def user_help(message: Message):
    await message.answer(f'/start - Запустити бота\n'
                         f'\n/svitlo - перевірити наявність світла\n'
                         f'\n/save_address - зберегти адресу(перед збереженням, переконайтесь у правильності написання адреси)\n'
                         f'\n{"-" * 20}'
                         f'\nЯкщо ви не можете знайти свою вулицю, перевірте її написання у https://www.dtek-kem.com.ua/ua/shutdowns'
                         f'\n{"-" * 20}'
                         f'\nЗа усіма пропозиціями щодо проєкту або співробітництва писати @ebduxi'
                         f'\n{"-" * 20}'
                         f'\n\u2615Buy me a coffee: buymeacoffee.com/shaxeno')
