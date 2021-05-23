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

button1 = KeyboardButton('Категории')
button2 = KeyboardButton('Подробно')
button3 = KeyboardButton('Помощь')

class MyPaginator(InlineKeyboardPaginator):
    first_page_label = '<<'
    previous_page_label = '<'
    current_page_label = '-{}-'
    next_page_label = '>'
    last_page_label = '>>'

category_menu = ReplyKeyboardMarkup()
fetchCategory = FetchCategory(category_urls)
for category in fetchCategory.get_category_list():
    category_btn = KeyboardButton(category.name)
    category_menu.insert(category_btn)