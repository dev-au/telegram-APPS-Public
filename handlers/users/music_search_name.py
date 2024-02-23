import asyncio

from aiogram.types import *

from data.music_controller import MusicSearcher
from keyboards.keyboards import KeyboardSetter
from loader import dp


@dp.message_handler()
async def recieve_text(message: Message):
    msg = await message.answer("🎵")
    await asyncio.sleep(1)
    try:
        search_term = message.text
        searcher = MusicSearcher()
        keyboarder = KeyboardSetter()
        search_result = await searcher.music_viewer(search_term, "search")
        keyboard = await keyboarder.search_result_keyboard(search_result, search_term)
        musics_info = ""
        line = 1
        for info in search_result[0][0]:
            musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
            line += 1
        await msg.delete()
        await message.answer_chat_action(ChatActions.TYPING)
        await asyncio.sleep(1)
        await message.reply(text=musics_info, reply_markup=keyboard)
    except:
        await msg.delete()
        await message.reply("Hech narsa topilmadi!")
