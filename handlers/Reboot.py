import os
import shutil
import asyncio
from git import Repo
from config import SUDO_USERS
from pyrogram.types import Message
from pyrogram import filters, Client
from git.exc import GitCommandError, InvalidGitRepositoryError

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["restart", "stop"], ["."]))
async def restart(client, m: Message):
    reply = await m.reply_text("🚑")     
    await m.delete() 
    await reply.edit(
        "<b>🔴Sedang Reboot!.</b>"
    )
    os.system(f"kill -9 {os.getpid()} && python3 main.py")
