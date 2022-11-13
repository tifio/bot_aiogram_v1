from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
import random

from config import TOKEN
from keyboards.keyboards import kb, kb_photo

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

HELP_COMAND = """
<b>/start</b> - <em>Запуск бота</em>
<b>/help</b> - <em>Список команд</em>
<b>/description</b> - <em>Описание бота</em>
"""

arr_photos = ["https://clck.ru/X7LB4",
              "https://clck.ru/aqm46",
              "https://clck.ru/TomgD"]


async def on_startup(_):
    print('---------------Bot started---------------')


@dp.message_handler(Text(equals='Random photo'))
async def open_kb_photo(message: types.Message):
    await message.answer(text='Нажми на "Рандом", чтобы получить фото',
                         reply_markup=kb_photo)
    await message.delete()

@dp.message_handler(Text(equals='Рандом'))
async def send_random_photo(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random.choice(arr_photos))
    await message.delete()


@dp.message_handler(Text(equals='Главное меню'))
async def open_kb(message: types.Message):
    await message.answer(text='Вы перешли в главное меню',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(text='Вы запустили бота 🫡',
                         reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.answer(text=HELP_COMAND,
                         parse_mode='HTML')
    await message.delete()


@dp.message_handler(commands=['description'])
async def cmd_description(message: types.Message):
    await message.answer(text='Бот умеет отправлять рандомные фотки',
                         reply_markup=kb)
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker='CAACAgIAAxkBAAEGaYBjcXOb4scm9CYn6MXiH2FrRUeO_QACnhgAAozDoEqPg4_NXMg8lisE')
    await message.delete()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
