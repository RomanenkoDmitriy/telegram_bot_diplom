from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


kb = [
    [KeyboardButton(text='All Work'), KeyboardButton(text='Blueprint')],
]

keyboard = ReplyKeyboardMarkup(keyboard=kb, one_time_keyboard=True, resize_keyboard=True)