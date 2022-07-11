import asyncio
import random
from asyncio import sleep

from pyrogram import filters
from pyrogram.types import Message

from pyrogram import Client
from main import *
SUDO = SUDO_USERS

@Client.on_message(filters.me & filters.command(["q", "quote"], '.'))
async def quotly(bot: Client, message: Message):
    if not message.reply_to_message:
        await message.edit("Balas pesan teks pengguna mana pun.")
        return

    await message.edit("```Sedang Mengkuot```")

    await message.reply_to_message.forward("@QuotLyBot")

    is_sticker = False
    progress = 0

    while not is_sticker:
        try:
            await sleep(4)
            msg = await bot.get_history("@QuotLyBot", 1)
            print(msg)
            is_sticker = True
        except:
            await sleep(1)

            progress += random.randint(0, 5)

            if progress > 100:
                await message.edit('Tidak Kuot 😭 sedang Erorr.')
                return

            try:
                await message.edit("```Membuat Kuot\nProcessing {}%```".format(progress))
            except:
                await message.edit("ERROR")

    if msg_id := msg[0]['message_id']:
        await asyncio.gather(
            message.delete(),
            bot.forward_messages(message.chat.id, "@QuotLyBot", msg_id)
        )


from handlers.help import *
add_command_help(
    "quote",
    [
        [
            ".q",
            "To Make a Quote",
        ],
        [
            ".quote",
            "To Make a Quote",
        ],
    ],
)
