# import logging
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram.types.inline_keyboard import  InlineKeyboardButton, InlineKeyboardMarkup
from config import *
from main import *
from aiogram import Bot, Dispatcher, executor, types
import buttons  as kb
from telegram_bot_pagination import InlineKeyboardPaginator
from aiogram.types.input_media import InputMediaPhoto, InputMediaVideo
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# init categories   
fetchCategory = FetchCategory(category_urls)
fetchProduct = FetchProduct(products_urls)
fetchMessage = Message(message_urls)
addToCart = CartItem(cart_items_urls)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!", reply_markup=kb.menu_markup)


@dp.message_handler(commands=['Меню'])
async def process_start_command(message: types.Message):
    await message.reply(message.text[1:], reply_markup=kb.category_menu)

global counter

@dp.message_handler()
async def process_start_command(message: types.Message):
    commands = [cat.name for cat in fetchCategory.get_category_list()]
    category_dict = {cat.name:cat.slug for cat in fetchCategory.get_category_list()}
    if message.text in commands:
        products = fetchCategory.get_products_to_category(
            category_dict[message.text]
        )
        
        if len(products) > 0:
            async def send_character_page(message, page=1):
                paginator = InlineKeyboardPaginator(
                    len(products),
                    current_page=page,
                    data_pattern='character#{page}'
                )
                salom = f'''Навзвание: {products[page-1].name} \nЦена: {products[page-1].price}'''
                await bot.send_message(
                    message.chat.id,
                    "|",
                    reply_markup=paginator.markup,
                    parse_mode='Markdown'
                )
            
            async def sendImages(userID, page=1):                
                pictures = fetchProduct.get_photo_by_id(products[page-1].slug)
                photos = [
                    item.url for item in pictures
                ]

                salom = f'''Навзвание: {products[page-1].name} \nЦена: {products[page-1].price}'''
                await bot.send_photo(userID, photos[0], salom ,  parse_mode='Markdown')

            @dp.callback_query_handler(lambda call: call.data.split('#')[0]=='character')
            async def characters_page_callback(call):
                page = int(call.data.split('#')[1])
                await bot.delete_message(
                    call.message.chat.id,
                    call.message.message_id,
                )

                @dp.callback_query_handler(lambda c: c.data == 'ADD_TO_CART')
                async def process_callback_button1(callback_query: types.CallbackQuery):
                    cart_item = addToCart.add_to_cart(products[page-1].id, 1, 1)
                    if cart_item == 200:
                        await bot.answer_callback_query(callback_query.id,text='Успешно добавлен в корзину', show_alert=True)
                    else:
                        await bot.answer_callback_query(callback_query.id, text='Ошибка!Не улалось добавить в корзину', show_alert=True)
                    await bot.answer_callback_query(callback_query.id)
                    # await bot.send_message(callback_query.from_user.id, 'added to cart!')

                await message.reply("", reply=False, reply_markup=kb.cartKeyBoard)
                await sendImages(message.from_user.id, page)
                await send_character_page(call.message, page)


            
            await sendImages(message.from_user.id)
            await message.reply("Первая инлайн кнопка", reply_markup=kb.cartKeyBoard)
            await send_character_page(message)
        else:
            media = [InputMediaVideo("https://media2.giphy.com/media/14uQ3cOFteDaU/giphy.gif?cid=ecf05e475zqy5gchpw4cgmmoaxoo53hfpbd4mts9i5k4dw06&rid=giphy.gif&ct=g", 'ёжик и котятки')]
            await bot.send_media_group(message.from_user.id, media)
    elif message.text == 'Меню 🏘':
        await message.reply(message.text, reply_markup=kb.category_menu)

    elif message.text == 'О нас ℹ':
        msg = fetchMessage.get_message("privetstvie")
        await message.reply(msg, reply_markup=kb.menu_markup)

    elif message.text == 'Помощь ❓':
        msg = fetchMessage.get_message("pomosh")
        await message.reply(msg, reply_markup=kb.menu_markup)
    else:
        await message.reply(message.text, reply_markup=kb.menu_markup)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)