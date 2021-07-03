import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from telethon.tl import functions
from telethon.tl.types import InputMessagesFilterDocument
from userbot import CMD_HELP, AUTO_PP, ASYNC_POOL
from userbot.events import register
import asyncio
import random
import shutil
import requests
import time
from telethon.errors import VideoFileInvalidError
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("autopp")

# ████████████████████████████████ #


@register(outgoing=True, pattern="^.autovideo ?(.*)$")
async def autovideo(event):
    if 'autovideo' in ASYNC_POOL:
        await event.edit(LANG['VIDEO_ALREADY_CHANGING'])
        return

    if not event.reply_to_msg_id:
        return await event.edit(LANG['NEED_VIDEO'])
    else:
        await event.edit(LANG['SETTING_VIDEO'])
        
        
        reply = await event.get_reply_message()
        video = await reply.download_media()
        yazi = event.pattern_match.group(1)

    try:
        os.remove("./pp.mp4")
    except:
        pass

    try:
        await event.client(functions.photos.UploadProfilePhotoRequest(
            video=await event.client.upload_file(video)
        ))
    except VideoFileInvalidError:
        return await event.edit(LANG['INVALID_VIDEO'])
    
    ASYNC_POOL.append('autovideo')

    await event.edit(LANG['STARTED_VIDEO'])
    while "autovideo" in ASYNC_POOL:
        saat = time.strftime("%H\.%M")
        tarih = time.strftime("%d\/%m\/%Y")

        if yazi:
            yazi = yazi.replace("$saat", saat).replace("$tarix", tarih)
            KOMUT = f"text=\'{yazi}\' :expansion=normal: y=h-line_h-10:x=(mod(5*n\,w+tw)-tw): fontcolor=white: fontsize=30: box=1: boxcolor=black@0.5: boxborderw=5: shadowx=2: shadowy=2"
        else:
            KOMUT = f"text=\'Saat\: {saat} Tarix\: {tarih} {yazi}\' :expansion=normal: y=h-line_h-10:x=(mod(5*n\,w+tw)-tw): fontcolor=white: fontsize=30: box=1: boxcolor=black@0.5: boxborderw=5: shadowx=2: shadowy=2"

        ses = await asyncio.create_subprocess_shell(f"ffmpeg -y -i '{video}' -vf drawtext=\"{KOMUT}\" pp.mp4")
        await ses.communicate()

        await event.client(functions.photos.UploadProfilePhotoRequest(
            video=await event.client.upload_file("pp.mp4")
        ))
        os.remove("./pp.mp4")
        await asyncio.sleep(60)

    os.remove(video)



CmdHelp('autovideo').add_command(
    'autopp', None, 
    'Bu əmr cavab verdiyiniz videonu profil videosu edər və bir saat və ya tarix və ya istədiyiniz bir yazı əlavə edər. Bu saat her dəqiqə dəyişir. ',
    '.autovideo cyber saat $saat bu da tarix $tarix'
).add()
