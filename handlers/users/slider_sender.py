from aiogram.types import *

from data.music_controller import MusicSearcher
from keyboards.keyboards import KeyboardSetter
from loader import dp


@dp.callback_query_handler(text_contains="^")
async def send_music(call: CallbackQuery):
    msg = await call.message.answer("🎶")
    await call.answer()
    musics = call.message.text.split("\n")
    music_id = call.data.split("^")[1]
    ind = int(call.data.split("^")[0])
    searcher = MusicSearcher()
    for music in musics:
        music_ind = int(music.split(".")[0])
        if music_ind == ind:
            search_term = music[music.index(".") + 1:]
            url = await searcher.get_video_url(music_id, search_term)
            await searcher.send_youtube_audio(url, call.from_user.id, search_term)
            await msg.delete()
            break


@dp.callback_query_handler(text_contains="~")
async def slider(call: CallbackQuery):
    searcher = MusicSearcher()
    keyboarder = KeyboardSetter()
    search_term = call.data.split("~")[1]
    now_page = call.data.split("~")[0]
    search_result = await searcher.music_viewer(search_term, f"slide-{now_page}")
    if search_result[0] == False:
        searcher = MusicSearcher()
        keyboarder = KeyboardSetter()
        search_result = await searcher.music_viewer(search_term, "search")
        keyboard = await keyboarder.search_result_keyboard(search_result, search_term)
        musics_info = ""
        line = 1
        for info in search_result[0][0]:
            musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
            line += 1
        return await call.message.edit_text(text=musics_info, reply_markup=keyboard)
    keyboard = await keyboarder.search_result_keyboard(search_result, search_term)
    musics_info = ""
    line = 1
    for info in search_result[0][0]:
        musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
        line += 1
    await call.message.edit_text(text=musics_info, reply_markup=keyboard)
