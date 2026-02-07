import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile
from aiogram import F 
from aiogram.utils.keyboard import ReplyKeyboardBuilder  
from variables import *
import os
from aiohttp import web

TOKEN = '7884118333:AAHeAFG6m16Fedht9HPxd6vMcb8urj_8qBc' #os.getenv('BOT_TOKEN')


bot = Bot(token=TOKEN)
dp = Dispatcher()

# ---  ДЛЯ RENDER ---
async def handle(request):
    return web.Response(text="Bot is running!")

async def start_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    # Render сам подставит порт в переменную среды PORT
    port = int(os.environ.get("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
# -------------------------------------------

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
    await start_server()
    await dp.start_polling(bot)


asyncio.run(main())
