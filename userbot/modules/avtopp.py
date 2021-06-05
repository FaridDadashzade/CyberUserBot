from userbot import CYBER_VERSION
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl import functions 
from telethon.tl.types import InputMessagesFilterDocument 
from userbot.events import register 
import requests 
import time 
from PIL import Image 
import datetime 
from PIL import Image, ImageDraw, ImageFont 
import os 
import asyncio 
import random 
from time import sleep
import os
from telethon.tl.functions.photos import (DeletePhotosRequest, GetUserPhotosRequest, UploadProfilePhotoRequest)
from telethon.tl.types import InputPhoto, MessageMediaPhoto, User, Chat, Channel
import os
async def get_font_file(client, channel_id):
    font_file_message_s = await client.get_messages(
        entity=channel_id,
        filter=InputMessagesFilterDocument,
        limit=None
    )
    font_file_message = random.choice(font_file_message_s)
    return await client.download_media(font_file_message)
async def saatpp(event):
    replymsg = await event.get_reply_message()
    photo = None
    if replymsg.media:
        if isinstance(replymsg.media, MessageMediaPhoto):
            photo = await event.client.download_media(message=replymsg.photo)
            foto = Image.open(photo)
            current_time = datetime.datetime.now().strftime("%H:%M") 
            f = await get_font_file(event.client, "@FontDunyasi")
            new = foto.resize((500,500)) 
            new.save("sonpp.jpg") 
            img = Image.open("sonpp.jpg") 
            drawn_text = ImageDraw.Draw(img) 
            fnt = ImageFont.truetype(f, 65) 
            size = drawn_text.multiline_textsize(current_time, font=fnt) 
            drawn_text.text(((img.width - size[0]) / 2, (img.height - size[1])),
                       current_time, font=fnt, fill=(255, 255, 255))
            img.save("sonpp.jpg")

@register(outgoing=True, pattern="^.avtopp$")
async def main(event):
  if not event.is_reply:
    return await event.edit('`Bir fotoya yanıt verin!`')
  else:
    await event.edit("`pp tənzimləndi..`")
  while True:
    await saatpp(event)
    await event.client(UploadProfilePhotoRequest(await event.client.upload_file("sonpp.jpg")))
    await asyncio.sleep(60) 
    await event.client(functions.photos.DeletePhotosRequest(await event.client.get_profile_photos("me", limit=1)))


CmdHelp('avtopp').add_command(
    'avtopp', None, ' Yanıt verilən fotonu AutoPP edir. '
).add()
