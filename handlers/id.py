from pyrogram import Client, filters
import asyncio
import time
from pyrogram.types import ChatPermissions, Message
from handlers.help import *


@Client.on_message(filters.me & filters.command("id", ["."]))
async def id(client: Client, message: Message):
    if message.reply_to_message is None:
        await message.reply(f"Chat ID: {message.chat.id}")
    else:
        test = f"<b>User ID:</b> {message.reply_to_message.from_user.id}\n\n<b>Chat ID:</b> {message.chat.id}"
        await message.edit_text(test)


add_command_help(
    "id",
    [
        [".id", "Lihat User ID."],
    ],
)
