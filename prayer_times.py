import logging
from aiogram import Bot, Dispatcher, executor, types
import aiohttp
API_TOKEN = 'Your Api Token'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def main(message:types.Message):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.aladhan.com/v1/calendarByAddress/2023/2?address={message.text}&method=2") as resp:
            import time
            today=time.localtime().tm_mday
            response=await resp.json()
            data=response["data"][today-1]["timings"]
            await message.answer(data)
            answer=f"🔷Quyosh chiqishi----⏱{data['Sunrise']}\n" \
                   f"🔷Peshin------------------⏱{data['Dhuhr']}\n" \
                   f"🔷Asr-----------------------⏱{data['Asr']}\n" \
                   f"🔷Quyosh botishi-----⏱{data['Sunset']}\n" \
                   f"🔷Yarim tun-------------⏱{data['Midnight']}"
            await message.answer(answer)
@dp.message_handler()
async def send_welcome(message: types.Message):
    await main(message)

executor.start_polling(dp, skip_updates=True)