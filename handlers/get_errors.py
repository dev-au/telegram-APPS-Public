from current_bot import *
from loguru import logger
import asyncio


error_router = Router()


@error_router.error()
async def error_handler(event: types.ErrorEvent):
    logger.add("logs.txt")
    logger.exception(event.exception)
    await bot.send_message(chat_id=ADMINS[0], text=f"ERROR!\n\n<code>{event.exception}</code>")
    file = types.FSInputFile("logs.txt")
    await asyncio.sleep(0.05)
    await bot.send_document(chat_id=ADMINS[0], document=file)


dp.include_router(error_router)
