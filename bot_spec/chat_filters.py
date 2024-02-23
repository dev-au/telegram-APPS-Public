from aiogram import filters
from aiogram import types
from aiogram.enums import chat_type
from current_bot import ADMINS


class IsChatGroup(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type in [chat_type.ChatType.SUPERGROUP, chat_type.ChatType.GROUP]


class IsChatSuperGroup(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == chat_type.ChatType.SUPERGROUP


class IsChatSimpleGroup(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == chat_type.ChatType.GROUP


class IsChatPrivate(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == chat_type.ChatType.PRIVATE


class IsChatChannel(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return message.chat.type == chat_type.ChatType.CHANNEL


class IsUserAdmin(filters.Filter):
    async def __call__(self, message: types.Message) -> bool:
        return int(message.chat.id) in ADMINS
