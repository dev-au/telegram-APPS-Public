from aiogram import types
from loader import dp

@dp.message_handler(commands=["help"])
async def echo(message: types.Message):
    url="Batafsil yo'riqnoma\n" \
        "https://telegra.ph/Kino-qidiruvchi-botdan-filmni-qidirish-01-06"
    await message.answer(url)

@dp.message_handler(commands=["t_help"])
async def echo(message: types.Message):
    text="Buning uchun video ostidagi yuklab olish tugmalarini bosib turing va url manzildan nusxa olib" \
         " https://t.me/urluploadxbot botiga yuboring shu yerdan siz keyin yuklab olishingiz mumkin"
    await message.answer(text)