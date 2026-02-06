import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram import F  # новый импорт!
from aiogram.utils.keyboard import ReplyKeyboardBuilder  # новый импорт!
from variables import *
import os

TOKEN = '7884118333:AAHeAFG6m16Fedht9HPxd6vMcb8urj_8qBc' #os.getenv('BOT_TOKEN')


bot = Bot(token=TOKEN)
dp = Dispatcher()



@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(helo)


@dp.message(Command('release'))
async def cmd_release(message: Message):
    await message.answer(https_release)

@dp.message(Command('img'))
async def cmd_img(message: Message):
    image = FSInputFile(img)
    await message.answer_photo(image, caption = '=)')

async def main():
    await dp.start_polling(bot)


asyncio.run(main())
