import logging
from config import API_TOKEN
from main import fetch_otus_json_data
from aiogram import Bot, Dispatcher, executor, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    for fif in fetch_otus_json_data():
        product_name = fif["product"][0]
        product_image = fif["product"][1]
        await message.answer(product_name)
        await bot.send_photo(message.chat.id, types.InputFile.from_url(product_image))

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)