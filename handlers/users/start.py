from aiogram.dispatcher.filters import CommandStart
from aiogram.types import *
from loader import dp


@dp.message_handler(CommandStart())
async def command_start(msg: Message):
    await msg.reply(f"Assalomu alaykum {msg.from_user.full_name} botga xush kelibsiz. Menga shunchaki musiqa nomini "
                    f"yoki ovozli parchasi yoki qisqa videosini tashlasangiz men sizga uni topib beraman.\n"
                    f"O'zbekistondagi hozirda trendda bo'lgan qo'shiqlarni yuklash uchun /top buyrug'ini bosing.")
