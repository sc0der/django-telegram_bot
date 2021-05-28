import logging
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
    await message.reply("Привет!", reply_markup=kb.category_menu)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, 'Нажата первая кнопка!')

@dp.message_handler(commands=['Помощь'])
async def process_start_command(message: types.Message):
    await message.reply(message.text[1:], reply_markup=kb.markup5)


@dp.message_handler()
async def process_start_command(message: types.Message):
    commands = [cat.name for cat in fetchCategory.get_category_list()]
    category_dict = {cat.name:cat.slug for cat in fetchCategory.get_category_list()}
    if message.text in commands:
        products = fetchCategory.get_products_to_category(
                category_dict[message.text]
            )
        # http://localhost:8000/photo_archive/products/n21ooj7vyeyvmfule7bjxxy0yqutjd.png

        # for prod in products:
        prod = products[0]
        photo = fetchProduct.get_photo_by_id(prod.slug)
        photos = []
        # for foto in photo:
        #     photos.append(
        #         InputMediaPhoto(
        #             "http://localhost:8000/photo_archive/products/n21ooj7vyeyvmfule7bjxxy0yqutjd.png",
        #             foto['photo'],
        #             ''
        #         )
        #     )

        photos.append(
                InputMediaPhoto(
                    "https://cdn.wallpapersafari.com/93/32/64OhnG.jpg",
                    'photo'
                )
            )

        print("prod: ", prod.name)
        print("prod_slg: ", prod.slug)
        print("prod_price: ", prod.price)
        # print("products: ", photos[0])

        # print('photo: ', photos[1])
        # photos.append(host + photo[0]['photo'])
        # paginator = kb.MyPaginator(len(products))
        await bot.send_media_group(message.from_user.id, photos)
        # await message.reply(prod.name, reply_markup=paginator.markup)
    else:
        print('nest')
        await message.reply('kuku: ' + message.text, reply_markup=kb.category_menu)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)