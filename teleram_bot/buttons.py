from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from main import FetchCategory
from config import *

button1 = KeyboardButton('Категории')
button2 = KeyboardButton('Подробно')
button3 = KeyboardButton('Помощь')


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)



category_menu = ReplyKeyboardMarkup()
testFetchCategory = FetchCategory(category_urls)
categ_list = testFetchCategory.get_category_list()
for category in categ_list:
    category_btn = KeyboardButton(category.name)
    category_menu.insert(category_btn)