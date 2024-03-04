import asyncio
from loguru import logger
from aiogram import types
from current_bot import bot, dp, ADMINS
from data.on_startup import *
import middlewares, handlers


async def bot_runner() -> None:
    await dp.start_polling(bot)


async def bot_on_startup() -> None:
    bot_user_name = (await bot.get_me()).username
    logger.info(runner_console_message(bot_user_name))
    await bot.send_message(ADMINS[0], runner_admin_message())
    commands = list()
    for command_name, command_description in bot_commands().items():
        commands.append(types.BotCommand(command=command_name, description=command_description))
    await bot.set_my_commands(commands)


async def main():
    await asyncio.gather(bot_runner(), bot_on_startup())


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("This bot successfully stopped!")
