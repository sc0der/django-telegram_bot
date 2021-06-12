from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from telegram_bot_pagination import InlineKeyboardPaginator
from main import FetchCategory
from config import *


addToCartBtn = InlineKeyboardButton('Добавить в корзину!', callback_data='ADD_TO_CART')
cartKeyBoard = InlineKeyboardMarkup().add(addToCartBtn)

menu_markup = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton('Меню 🏘')
button2 = KeyboardButton('О нас ℹ')
button3 = KeyboardButton('Помощь ❓')
menu_markup.row(button1)
menu_markup.row(button2)
menu_markup.row(button3)

remoteKeyBoard = ReplyKeyboardRemove()
category_menu = ReplyKeyboardMarkup(resize_keyboard=True)
fetchCategory = FetchCategory(category_urls)
for category in fetchCategory.get_category_list():
    category_btn = KeyboardButton(category.name)
    category_menu.add(category_btn)
cartKb = KeyboardButton("Корзина 🗑")    
category_menu.add(cartKb)



# paginator
class KbPaginator(object):
    
    def __init__(self, objects):
        self.objects = objects

    def buil_kb(self):
        inline_markup = InlineKeyboardMarkup()
        for kb in range(len(self.objects)):
            inline_markup.add(InlineKeyboardButton(f'{kb}', callback_data=f'{kb}'))
