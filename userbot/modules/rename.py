# Copyright 2021 (C) FaridDadashzade
#
# TG: @faridxz

import os
import time
from datetime import datetime

from userbot.cmdhelp import CmdHelp
from userbot import CYBER_VERSION
from datetime import date
from userbot import TEMP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
from userbot.utils import progress

thumb_image_path = TEMP_DOWNLOAD_DIRECTORY + "/thumb_image.jpg"


@register(outgoing=True, pattern=r"^\.rename(?: |$)(.*)")
async def rename(event):
    if event.fwd_from:
        return
    thumb = None
    if os.path.exists(thumb_image_path):
        thumb = thumb_image_path
    await event.edit("Fayl adı dəyişdirilir..\nBiraz gözləyin...")
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        end = datetime.now()
        file_name = input_str
        reply_message = await event.get_reply_message()
        to_download_directory = TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await bot.download_media(
            reply_message,
            downloaded_file_name,
        )
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await event.client.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=True,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit(
                "{} saniyədə yükləndi və {} saniyə içində hazırlandı.".format(
                    ms_one, ms_two
                )
            )
        else:
            await event.edit("{} adlı fayl tapılmadı.".format(input_str))
    else:
        await event.edit("İstifadəsi: .rename [fayla_cavab] yeniad.ad")
        
        
Help = CmdHelp('rename')
Help.add_command('rename', '<fayla cavab>', 'Seçdiyiniz faylın adını dəyişdirər.')
Help.add_info('@faridxz tərəfindən @TheCyberUserBot üçün hazırlanmışdır.')
Help.add()                  
