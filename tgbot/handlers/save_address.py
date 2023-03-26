from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from tgbot.misc.states import Address
from tgbot.keyboards.reply import address_keyboard

router = Router(name='save_address')


@router.message(Command(commands=['save_address']))
async def user_save_address(message: Message, state: FSMContext):
    await message.answer(f'Введіть назву вулиці за такою формою:'
                         f'\n*назва вулиці, номер вулиці*')
    await state.set_state(Address.save_address)


@router.message(Address.save_address)
async def address_saved(message: Message, state: FSMContext):
    if message.text:
        await state.update_data()
        await message.answer(f'Чудово', reply_markup=address_keyboard(f'/svitlo {message.text}'))
        await state.clear()
