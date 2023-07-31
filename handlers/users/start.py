from aiogram import types
from keyboards.inline.main_keyboards import *
from loader import dp

@dp.message_handler(commands=["start"])
async def bot_start(message: types.Message):
    await message.answer("Assalomu alaykum Film qidirish botiga xush kelibsiz!!"
                         " Kino topish uchun pastdagi tugmani bosib kino nomini yozing "
                         "va kerakli kinoni ustiga bosing.\nAgar botdan qanday foydalanishni bilmayotgan bo'lsangiz /help ni bosing",reply_markup=start_menu)