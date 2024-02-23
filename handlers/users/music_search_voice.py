import asyncio
from io import BytesIO

from aiogram.types import ChatActions, Message

from data.music_controller import MusicSearcher
from keyboards.keyboards import KeyboardSetter
from loader import dp


@dp.message_handler(content_types=["voice", "audio"])
async def search_by_voice(message: Message):
    await message.answer_chat_action(ChatActions.RECORD_VOICE)
    await asyncio.sleep(3)
    searcher = MusicSearcher()
    audio_bytes = BytesIO()
    try:
        voice = message.voice
        file_id = voice.file_id
    except:
        voice = message.audio
        file_id = voice.file_id

    await voice.download(destination_file=audio_bytes)
    audio_bytes.seek(0)
    audio_bytearray = audio_bytes.getvalue()

    try:
        song_name = await searcher.search_music_by_voice(audio_bytearray)
        keyboarder = KeyboardSetter()
        search_result = await searcher.music_viewer(song_name, "search")
        keyboard = await keyboarder.search_result_keyboard(search_result, song_name)
        musics_info = ""
        line = 1
        for info in search_result[0][0]:
            musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
            line += 1
        await message.answer_chat_action(ChatActions.TYPING)
        await asyncio.sleep(1)
        await message.answer_chat_action(ChatActions.TYPING)
        await message.reply(text=musics_info, reply_markup=keyboard)
    except:
        await message.reply("Hech narsa topilmadi!")


@dp.message_handler(content_types="video")
async def search_by_video(message: Message):
    audio_bytes = BytesIO()
    await message.video.download(destination_file=audio_bytes)
    audio_bytearray = audio_bytes.getvalue()
    searcher = MusicSearcher()
    try:
        song_name = await searcher.search_music_by_voice(audio_bytearray)
        keyboarder = KeyboardSetter()
        search_result = await searcher.music_viewer(song_name, "search")
        keyboard = await keyboarder.search_result_keyboard(search_result, song_name)
        musics_info = ""
        line = 1
        for info in search_result[0][0]:
            musics_info += f"{line}.{info[0][0]} ~ {info[0][1]}\n"
            line += 1
        await message.answer_chat_action(ChatActions.TYPING)
        await asyncio.sleep(1)
        await message.answer_chat_action(ChatActions.TYPING)
        await message.reply(text=musics_info, reply_markup=keyboard)
    except:
        await message.reply("Hech narsa topilmadi!")
