import logging
from telegram_bot_pagination import InlineKeyboardPaginator
from data import character_pages
from config import API_TOKEN
from main import *
from aiogram import Bot, Dispatcher, executor, types
from telegram_bot_pagination import InlineKeyboardPaginator
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, page=1):
    paginator = InlineKeyboardPaginator(
        len(character_pages),
        current_page=page,
        
        data_pattern='character#{page}'
    )

    await bot.send_message(
        message.chat.id,
        character_pages[page-1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )
    name = message.from_user.id
    print("user_data: ", name)
    await message.answer(name)
    # for item in fetch_otus_json_data():
    #     product_name = item["product"][0]
    #     product_image = item["product"][1]
    #     await message.answer(product_name)
    #     await bot.send_photo(message.chat.id, types.InputFile.from_url(product_image))

    async def characters_page_callback(call):
        page = int(call.data.split('#')[1])
        bot.delete_message(
            call.message.chat.id,
            call.message.message_id
        )
        await send_welcome(call.message, page)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)