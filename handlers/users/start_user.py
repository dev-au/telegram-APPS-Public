from imports import *
from sqlite3 import IntegrityError


@dp.message_handler(CommandStart())
async def start_bot_command(message: types.Message):
    user_id = message.from_user.id
    text = message.text
    try:
        db.add_user(user_id, message.from_user.language_code)
        await message.answer(f"Xush kelibsiz {message.from_user.full_name}")
    except IntegrityError:
        await message.answer("Salom")
