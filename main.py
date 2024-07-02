import asyncio
import logging
from io import BytesIO
import os

import requests
from PIL import Image

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import TOKEN, URL_SVER
from key_board import keyboard

bot = Bot(token=TOKEN)
dispatcher = Dispatcher()


@dispatcher.message(CommandStart())
async def welcome(message: Message):
    await message.answer(text='Hello', reply_markup=keyboard)


@dispatcher.message(F.text == 'All Work')
async def all_work(message: Message):
    url = f'{URL_SVER}/api/completed_work/'
    response = requests.get(url).json()
    for product in response['results']:
        title = product['title']
        description = product['description']
        overall_plan = product['overall_plan']
        await message.answer(text=f'{title}\n\n{description}\n\n{overall_plan}')


@dispatcher.message(F.text == 'Blueprint')
async def blueprint(message: Message):
    url = f'{URL_SVER}/api/blueprint/'
    response = requests.get(url).json()
    # await message.answer(text=f'{response}')
    for blueprints in response:
        title = blueprints['title']
        file_pdf = f'{URL_SVER}{blueprints["file_pdf"]}'
        file_dwg = f'{URL_SVER}{blueprints["file_dwg"]}'
        file_b3d = f'{URL_SVER}{blueprints["file_b3d"]}'

        await message.answer(f'{title}\n\n{file_pdf}\n\n{file_dwg}\n\n{file_b3d}')


async def main():
    logging.basicConfig(level=logging.INFO)
    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
