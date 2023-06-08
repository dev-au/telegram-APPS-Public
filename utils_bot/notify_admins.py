


async def admins_note(notify_text: str):
    import logging
    from . import dp
    from data import ADMINS
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, notify_text, disable_notification=False)
        except Exception as err:
            logging.exception(err)
