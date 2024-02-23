from aiogram.enums import ParseMode
from environs import Env
from aiogram import (types, filters, Router, Dispatcher, Bot)
from bot_spec import local_translator
from data.languages_text import languages, all_text
from data.sqlite_db import UsersTable

env = Env()
env.read_env()
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = list(map(int, env.list("ADMINS")))
bot = Bot(BOT_TOKEN, parse_mode=ParseMode.HTML)
dp = Dispatcher()
_ = local_translator.LanguageTranslator(languages, all_text)

user_table = UsersTable()
