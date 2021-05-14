from aiogram.types import (
    ReplyKeyboardRemove,
    ReplyKeyboardMarkup, 
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

button1 = KeyboardButton('Категории')
button2 = KeyboardButton('Наш канал')
button3 = KeyboardButton('Помощь')

markup3 = ReplyKeyboardMarkup().add(
    button1).add(button2).add(button3)

markup5 = ReplyKeyboardMarkup()
markup5.add(button1)
markup5.add(button2)
markup5.add(button3)
# markup5.insert(markup3)