import sqlite3

from current_bot import _, filters, types, dp, user_table
from aiogram import F


@dp.message(filters.CommandStart())
async def start_command(message: types.Message):
    try:
        user_table.add_row(
            telegram_id=message.chat.id,
            full_name=message.from_user.full_name,
            first_message="none"
        )
        await message.answer("hi new user")
    except sqlite3.IntegrityError:
        await message.reply(_.uz("hello").format(name=message.from_user.full_name))


@dp.message()
async def first_message(message: types.Message):
    old_user = user_table.select_row(telegram_id=message.chat.id)
    if old_user[-1] == "none":
        user_table.update_row(
            {
                "telegram_id": message.chat.id
            },
            "first_message",
            message.text
        )
        await message.answer(f"You are first message is now updated. Message is {message.text}")
    else:
        await message.answer(f"You have already joined database! You first message is {old_user[-1]}")


@dp.message(F.text == "ok")
async def filtered(message: types.Message):
    await message.reply("working filter")
