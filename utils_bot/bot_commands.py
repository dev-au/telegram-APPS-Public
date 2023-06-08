async def set_bot_commands(bot_commands: dict):
    from aiogram.types import BotCommand
    from .loader import dp
    commands_list = []
    for command_name, command_info in bot_commands.items():
        commands_list.append(BotCommand(command_name, command_info))
    await dp.bot.set_my_commands(commands_list)