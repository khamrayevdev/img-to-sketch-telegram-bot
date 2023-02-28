import logging
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from img2sketch import imgtosketch

API_TOKEN = 'Bot token'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    cit = message.chat.id
    file_id = message.photo[-1].file_id
    file = await bot.get_file(file_id)
    url = f"https://api.telegram.org/file/bot{API_TOKEN}/{file.file_path}"
    imgtosketch(url)
    await bot.send_document(chat_id=cit, document=open('rasm.jpg', 'rb'))






if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

