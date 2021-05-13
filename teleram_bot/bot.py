import logging
from telegram_bot_pagination import InlineKeyboardPaginator
from data import character_pages
from config import API_TOKEN, members_urls
from main import *
from aiogram import Bot, Dispatcher, executor, types
from telegram_bot_pagination import InlineKeyboardPaginator
from aiogram_dialog import DialogManager
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram_dialog import Dialog
from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import Button
from aiogram_dialog.widgets.text import Const
from aiogram_dialog import DialogRegistry
from aiogram.contrib.fsm_storage.memory import MemoryStorage


class MySG(StatesGroup):
    main = State()


main_window = Window(
    Const("Hello, unknown person"),  # just a constant text
    Button(Const("Useless button"), id="nothing"),  # button with text and id
    state=MySG.main,  # state is used to identify window between dialogs
)


dialog = Dialog(main_window)


storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)
# channel_id = "1176153586"

registry = DialogRegistry(dp)  # this is required to use `aiogram_dialog`
registry.register(dialog) 

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message, dialog_manager: DialogManager, page=2, ):
    paginator = InlineKeyboardPaginator(
        len(character_pages),
        current_page=page,
        data_pattern='character#{page}'
    )

    await dialog_manager.start(MySG.main, reset_stack=True)

    await bot.send_message(
        message.chat.id,
        character_pages[page-1],
        reply_markup=paginator.markup,
        parse_mode='Markdown'
    )
    result = await bot.get_chat("@bursak_shop")
    isS = await bot.get_chat_member("-1001176153586", "563792320")
    print(isS)
    member = Member(urls=members_urls, message=message)
    
    mem_msg = member.add_new_member()
    await message.answer(result)
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