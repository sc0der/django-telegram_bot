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
global products
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

global g_key

# getting data from product list by index
# async def send_character_page(pages, message, page=1):
#     paginator = InlineKeyboardPaginator(pages, current_page=page, data_pattern='character#{page}')
#     await bot.send_message(message.chat.id, text=".", reply_markup=paginator.markup, parse_mode='Markdown')

# sending product in replay
# async def sendProductInfo(products, userID, page=1):    
#     pictures = fetchProduct.get_photo_by_id(products[page-1].slug)
#     photos = [item.url for item in pictures ]
#     # print("checking")
#     print("checking:", products[0].name)
#     description = f'''Навзвание: {products[page-1].name} \nЦена: {products[page-1].price}'''
#     await bot.send_photo(userID, photos[0], description, reply_markup=kb.cartKeyBoard,  parse_mode='Markdown', )

async def send_character_page(products, userID, page=1):
    pictures = fetchProduct.get_photo_by_id(products[page-1].slug)
    photos = [item.url for item in pictures ]
    paginator = InlineKeyboardPaginator(len(products), current_page=page, data_pattern='character#{page}')
    description = f'''Навзвание: {products[page-1].name} \nЦена: {products[page-1].price} \nОписание: {products[page-1].description} "/добавить" в корзину'''
    await bot.send_photo(userID, photos[0], description, reply_markup=paginator.markup, parse_mode='Markdown')
        # await bot.send_message(message.chat.id, text=".", reply_markup=paginator.markup, parse_mode='Markdown')

async def process_callback_button(callback_query: types.CallbackQuery, products, page):
    cart_item = addToCart.add_to_cart(products[page-1].id, 1, 1)
    if cart_item == 200:
        await bot.answer_callback_query(callback_query.id,text='Успешно добавлен в корзину', show_alert=True)
    else:
        await bot.answer_callback_query(callback_query.id, text='Ошибка! Не улалось добавить в корзину', show_alert=True)
    await bot.answer_callback_query(callback_query.id)


async def deleteMessage(call):
    await bot.delete_message(
        call.message.chat.id,
        call.message.message_id,
    )
async def refreshData(v_key):
    products = fetchCategory.get_products_to_category(
            v_key 
    )

    @dp.callback_query_handler(lambda call: call.data.split('#')[0]=='character')
    async def characters_page_callback(call):
        page = int(call.data.split('#')[1])
        print("testing page:", page)
        print(call)
        await deleteMessage(call=call)
        # await sendProductInfo(products, call.message.messa, page)
        await send_character_page(products, call.from_user.id, page)

@dp.message_handler()
async def process_start_command(message: types.Message):
    commands = [cat.name for cat in fetchCategory.get_category_list()]
    category_dict = {cat.name:cat.slug for cat in fetchCategory.get_category_list()}
    if message.text in commands:
        g_key = message.text
        products = fetchCategory.get_products_to_category(
            category_dict[g_key]
        )
        print("before: ", len(products))
        print("testing:", g_key)
        if len(products) > 0:
            await refreshData(v_key=category_dict[g_key])
            print("g_key: ", g_key)
            await send_character_page(products, message.from_user.id, )
            # await sendProductInfo(products, message.from_user.id)
            # await send_character_page(len(products), message)
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