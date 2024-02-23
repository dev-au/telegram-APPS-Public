import asyncio

from aiogram.types import *

from data.music_controller import MusicSearcher
from keyboards.keyboards import KeyboardSetter
from loader import dp


@dp.message_handler(text="/top")
async def top_uzbekistan(message: Message):
    msg = await message.answer("🎵")
    await asyncio.sleep(1)
    searcher = MusicSearcher()
    keyboarder = KeyboardSetter()
    search_result = await searcher.top_chart10("UZ")
    keyboard = await keyboarder.search_result_keyboard(search_result)
    musics_info = ""
    line = 1
    for info in search_result[0][0]:
        musics_info += f"{line}.{info[0][0]} ~  {info[0][1]}\n"
        line += 1
    await msg.delete()
    await message.reply(text=musics_info, reply_markup=keyboard)
