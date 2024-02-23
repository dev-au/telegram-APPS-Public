from random import randint
from aiogram.types import InputFile, ChatActions
from loader import bot
from shazamio import Shazam, Serialize
import aiohttp
import io
import pytube


class MusicSearcher:
    shazam = Shazam()

    async def async_requester(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                rsp = await resp.json()
                if len(rsp) == 0:
                    return False
                responser = []
                for item in rsp['tracks']['hits']:
                    try:
                        music_info = [item['track']['title'], item['track']['subtitle']]
                        music_id = item['track']['key']
                        responser.append([music_info, music_id])
                    except:
                        pass
                try:
                    next = rsp['tracks']['next']
                    is_next_url = True
                    if len(responser) != 10:
                        result = 10 - len(responser)
                        for nm in range(result):
                            number = randint(1, 10 - result) - 1
                            copy = responser[number]
                            responser.append(copy)
                except:
                    is_next_url = False
                return [responser, is_next_url]

    async def music_viewer(self, search_term, option="search_mixed"):
        now_page = 0
        if option.startswith("search"):
            complete_url = f"https://www.shazam.com/services/search/v4/en-US/UZ/web/search?term={search_term}&numResults=10&offset=0&types=songs,artists&limit=10"
        elif option.startswith("slide"):
            page = option.split("-")
            now_page = int(page[1])
            complete_url = f"https://cdn.shazam.com/search/v4/en-US/UZ/web/search?term={search_term}&offset={(now_page) * 10}&limit=10&types=songs,artists"
        else:
            return "Incorrect url!"
        return [await self.async_requester(complete_url), now_page]

    async def get_video_url(self, music_id, name):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                    f"https://www.shazam.com/video/v3/-/-/web/{music_id}/youtube/video?q={name}") as resp:
                rsp = await resp.json()
                return rsp['actions'][0]['uri']

    async def send_youtube_audio(self, url, chat_id, name):
        try:
            await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_AUDIO)
            pytube_audio = pytube.YouTube(url)
            publish_date = pytube_audio.publish_date
            duration = pytube_audio.length
            pytube_audio = pytube_audio.streams.filter(only_audio=True).first()
            audio_bytes = io.BytesIO()
            pytube_audio.stream_to_buffer(audio_bytes)
            audio_bytes.seek(0)
            music_name = name.split("~")[0]
            artist_name = name.split("~")[1]
            audio_file = InputFile(audio_bytes, filename=f"{music_name} - {artist_name}.mp3")
            await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_AUDIO)
            bot_info = await bot.get_me()
            username = bot_info.username
            await bot.send_chat_action(chat_id=chat_id, action=ChatActions.UPLOAD_AUDIO)
            await bot.send_audio(chat_id=chat_id, audio=audio_file, title=music_name, performer=artist_name,
                                 caption=f"{artist_name} - {music_name}\n"
                                         f"Premyera {str(publish_date).split(' ')[0]}\n"
                                         f"@{username}", duration=duration)
            audio_bytes.close()
        except Exception as error:
            pass
            await bot.send_message(chat_id=chat_id, text="Noma'lum xato! Musiqa bloklangan bo'lishi mumkin! Yoki "
                                                         "qayta urining", )

    async def search_music_by_voice(self, bytes_audio):

        song = await self.shazam.recognize_song(bytes_audio)
        name = song['track']['share']['subject']
        return name

    async def top_chart10(self, country_code):

        results = await self.shazam.top_country_tracks(country_code, limit=10)
        response = []
        for track in results['tracks']:
            serialized = Serialize.track(data=track)
            name = [serialized.title, serialized.subtitle]
            music_id = serialized.key
            response.append([name, music_id])
        return [[response, False], 0]
