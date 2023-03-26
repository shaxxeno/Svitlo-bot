from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def address_keyboard(user_text):
    kb = [[KeyboardButton(text=user_text)]]
    return ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
