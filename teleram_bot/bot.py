import logging
from config import API_TOKEN, members_urls
from main import *
from aiogram import Bot, Dispatcher, executor, types
import buttons  as kb
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.category_menu)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

@dp.message_handler(commands=['Помощь'])
async def process_start_command(message: types.Message):
    await message.reply(message.text[1:], reply_markup=kb.markup5)

@dp.message_handler(commands=['Подробно'])
async def process_start_command(message: types.Message):
    await message.reply('/' + message.text, reply_markup=kb.markup5)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)