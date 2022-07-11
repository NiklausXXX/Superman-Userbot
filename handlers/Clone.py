import os
from pyrogram import *
from handlers.help import *
from pyrogram.types import *
from helpers.basic import edit_or_reply, get_text, get_user


OWNER = os.environ.get("OWNER", None)
BIO = os.environ.get("BIO", "See my village 🏕️@kampungmaifudin")




@Client.on_message(filters.command('clone', ["."]) & filters.me)
async def clone(client: Client, message: Message):
  text = get_text(message)
  op = await edit_or_reply(message, "`Mengkelon`")
  userk = get_user(message, text)[0]
  user_ = await client.get_users(userk)
  if not user_:
    await op.edit("`Sapa yang mau dikelon :3`")
    return
    
  get_bio = await client.get_chat(user_.id)
  f_name = user_.first_name
  c_bio = get_bio.bio
  pic = user_.photo.big_file_id
  poto = await client.download_media(pic)

  await client.set_profile_photo(photo=poto)
  await client.update_profile(
       first_name=f_name,
       bio=c_bio,
  )
  await message.edit(f"**Mulai sekarang saya adalah ** __{f_name}__")
    

@Client.on_message(filters.command('revert', ["."]) & filters.me)
async def revert(client: Client, message: Message):
 await message.edit("`Kembali seperti Semula :)`")
 r_bio = BIO
	
	#Get ur Name back
 await client.update_profile(
	  first_name=OWNER,
	  bio=r_bio,
	)
	#Delte first photo to get ur identify
 photos = await client.get_profile_photos("me")
 await client.delete_profile_photos(photos[0].file_id)
 await message.edit("`Saya kembali.`")


add_command_help(
    "cloner",
    [
        [".clone", "Mengkelon."],
        [".revert", "Kembali seperti semula."],
    ],
)
