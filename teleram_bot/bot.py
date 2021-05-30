import logging

from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from config import *
from main import *
from aiogram import Bot, Dispatcher, executor, types
import buttons  as kb
from telegram_bot_pagination import InlineKeyboardPaginator
from aiogram.types.input_media import InputMediaPhoto
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# init categories   
fetchCategory = FetchCategory(category_urls)
fetchProduct = FetchProduct(products_urls)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.menu_markup)


@dp.message_handler(commands=['Меню'])
async def process_start_command(message: types.Message):
    await message.reply(message.text[1:], reply_markup=kb.category_menu)


@dp.message_handler()
async def process_start_command(message: types.Message):
    commands = [cat.name for cat in fetchCategory.get_category_list()]
    category_dict = {cat.name:cat.slug for cat in fetchCategory.get_category_list()}
    if message.text in commands:
        products = fetchCategory.get_products_to_category(
            category_dict[message.text]
        )
        prod = products[0]
        photo = fetchProduct.get_photo_by_id(prod.slug)
        photos = []
        paginator = InlineKeyboardPaginator(
                len(products),
                current_page=1,
                data_pattern='elements#{page}'
        )
        photos.append(
                InputMediaPhoto(
                    "https://developer-blogs.nvidia.com/wp-content/uploads/2017/10/numba_blue_icon_rgb.png",
                    'photo'
                )
            )

       
        await send_character_page(message)
        await bot.send_media_group(message.from_user.id, photos)

    elif message.text == 'Меню':
        await message.reply(message.text, reply_markup=kb.category_menu)

    elif message.text == 'О нас':
        await message.reply(message.text, reply_markup=kb.remoteKeyBoard)

    elif message.text == 'Помощь':
        await message.reply(message.text, reply_markup=kb.category_menu)
    else:
        await message.reply(message.text, reply_markup=kb.category_menu)


async def send_character_page(message, page=1):
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


@dp.callback_query_handler(lambda call: call.data.split('#')[0]=='character')
async def characters_page_callback(call):
    page = int(call.data.split('#')[1])
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id
    )
    await send_character_page(call.message, page)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)