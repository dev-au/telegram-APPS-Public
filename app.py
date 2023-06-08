from aiogram.utils.exceptions import NetworkError

from imports import *
from loguru import logger
import middlewares, filters, handlers


async def on_startup(dispatcher):
    logger.info("This bot succesfully started!")
    db.create_table_users()
    await admins_note("Bot ishga tushdi")
    await set_bot_commands(
        {
            "start": "Botni ishga tushirish",
            "help": "Yordam"
        }
    )


async def on_shutdown(dispatcher):
    logger.info("This bot succesfully stopped!")
    await dp.storage.close()
    await dp.storage.wait_closed()


if __name__ == "__main__":
        try:
            executor.start_polling(
                dp,
                on_startup=on_startup,
                on_shutdown=on_shutdown,
                skip_updates=True
            )
        except NetworkError:
            print("No Internet!")