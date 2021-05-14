import logging
from config import API_TOKEN, members_urls
from main import *
from aiogram import Bot, Dispatcher, executor, types
import buttons  as kb
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.markup5)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)