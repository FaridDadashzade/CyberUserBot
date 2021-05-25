# Copyright (C) 2021 Farid Dadashzade


import asyncio
import os
import time
import zipfile
from userbot.cmdhelp import CmdHelp
from userbot import CYBER_VERSION
from datetime import date

from userbot import TEMP_DOWNLOAD_DIRECTORY, ZIP_DOWNLOAD_DIRECTORY, bot
from userbot.events import register
from userbot.utils import progress

# ====================
today = date.today()
# ====================


@register(outgoing=True, pattern=r"^\.sıxışdır(?: |$)(.*)")
async def _(event):
    # CYBERUSERBOT #
    if event.is_channel and not event.is_group:
        await event.edit("**Bu əmr kanallarda işləmir!**")
        return
    if event.fwd_from:
        return
    if not event.is_reply:
        await event.edit("**Sıxışdırmaq üçün bir fayla cavab ver!**")
        return
    mone = await event.edit("**Hazırlanır...\nBiraz gözləyin..**")
    if not os.path.isdir(TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                TEMP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[YÜKLƏNİLİR]")
                ),
            )
            directory_name = downloaded_file_name
            await event.edit(
                f"`{directory_name}` yükləndi." "\nFayl sıxışdırılır...."
            )
        except Exception as e:
            await mone.edit(str(e))
    zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED).write(
        directory_name
    )
    c_time = time.time()
    await bot.send_file(
        event.chat_id,
        directory_name + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=event.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[Hazırlanır]")
        ),
    )
    await event.edit("**Bitdi...**")
    await asyncio.sleep(7)
    await event.delete()


@register(outgoing=True, pattern=r"^\.addzip(?: |$)(.*)")
async def addzip(add):
    """ Copyright (c) 2020 azrim @github"""
    if add.is_channel and not add.is_group:
        await add.edit("**Bu əmr kanallarda işləmir!**")
        return
    if add.fwd_from:
        return
    if not add.is_reply:
        await add.edit("**Bir Zip faylını öz serverimə yükləyə\nbilməyim üçün bir fayla cavab ver!**")
        return
    mone = await add.edit("**Hazırlanır...**")
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        os.makedirs(ZIP_DOWNLOAD_DIRECTORY)
    if add.reply_to_msg_id:
        reply_message = await add.get_reply_message()
        try:
            c_time = time.time()
            downloaded_file_name = await bot.download_media(
                reply_message,
                ZIP_DOWNLOAD_DIRECTORY,
                progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
                    progress(d, t, mone, c_time, "[Yüklənir]")
                ),
            )
            success = str(downloaded_file_name).replace("./zips/", "")
            await add.edit(f"`{success}` uğurla siyahıya əlavə edildi!")
        except Exception as e:  
            await mone.edit(str(e))
            return


@register(outgoing=True, pattern=r"^\.upzip(?: |$)(.*)")
async def upload_zip(up):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await up.edit("**Fayl tapılmadı.**")
        return
    mone = await up.edit("**Hazırlanır..\nBiraz gözləyin...**")
    input_str = up.pattern_match.group(1)
    curdate = today.strftime("%m%d%y")
    title = str(input_str) if input_str else "zipfile" + f"{curdate}"
    zipf = zipfile.ZipFile(title + ".zip", "w", zipfile.ZIP_DEFLATED)
    zipdir(ZIP_DOWNLOAD_DIRECTORY, zipf)
    zipf.close()
    c_time = time.time()
    await bot.send_file(
        up.chat_id,
        title + ".zip",
        force_document=True,
        allow_cache=False,
        reply_to=up.message.id,
        progress_callback=lambda d, t: asyncio.get_event_loop().create_task(
            progress(d, t, mone, c_time, "[Hazırlanır]", input_str)
        ),
    )
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await up.delete()


@register(outgoing=True, pattern=r"^\.rmzip(?: |$)(.*)")
async def remove_dir(rm):
    if not os.path.isdir(ZIP_DOWNLOAD_DIRECTORY):
        await rm.edit("**Fayl tapılmadı...**")
        return
    os.rmdir(ZIP_DOWNLOAD_DIRECTORY)
    await rm.edit("**Zip siyahısı uğurla təmizləndi!**")


def zipdir(path, ziph):
    # CYBERUSERBOT #
    for root, _, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
            
Help = CmdHelp('zip')
Help.add_command('sıxışdır', '<fayla cavab>', 'Bir faylı Zip faylına çevirər.')
Help.add_command('addzip', '<fayla cavab>', 'Cavab verdiyiniz faylı userbot serverinə yükləyər.')
Help.add_command('upzip', None, 'UserBot serverində olan bir faylı göndərər.')
Help.add_command('rmzip', None, 'Zip siyahısını təmizləyər.')
Help.add_info('@faridxz tərəfindən @TheCyberUserBot üçün hazırlanmışdır.')
Help.add()           
