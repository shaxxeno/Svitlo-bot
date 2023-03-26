from aiogram.fsm.state import StatesGroup, State


class Address(StatesGroup):
    save_address = State()
