from aiogram import Bot, Dispatcher, executor, types

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('---------------Bot started---------------')




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
