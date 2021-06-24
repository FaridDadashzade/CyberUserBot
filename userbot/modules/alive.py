# Copyright 2021 (C) CYBERUSERBOT
#
# Farid Dadashzade - CyberUserBot

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which
from os import remove
import time

from userbot import (
    ALIVE_LOGO,
    ALIVE_NAME,
    CYBER_VERSION,
    StartTime,
    bot,
)

from userbot.events import register
from userbot.cmdhelp import CmdHelp


# ================= CYBER =================
DEFAULTUSER = str(ALIVE_NAME)
# ============================================


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["saniyə", "dəqiqə", "saat", "gün"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time



@register(outgoing=True, pattern=r"^\.salive(?: |$)(.*)")
async def salive(alive):
    user = await bot.get_me()
    islememuddeti = await get_readable_time((time.time() - StartTime))
    kecid = (
        f"**✦ C Y B Σ R USERBOT ✦** \n"
        f"┏━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"┣[ 🧭 **Botun işləmə müddəti:** `{islememuddeti}`\n"
        f"┣[ 👤 **Mənim sahibim:** `{DEFAULTUSER}`\n"
        f"┣[ 🐍 **Python:** `3.8.6`\n"
        f"┣[ ⚙️ **Telethon:** `1.17.4`\n"
        f"┣[ 👁‍🗨 **İstifadəçi adı:** @{user.username}\n"
        f"┣[ 🗄 **Branch:** `Master`\n"
        f"┗━━━━━━━━━━━━━━━━━━━━━━━━\n"
        f"**C Y B Σ R:** `{CYBER_VERSION}`"
    )
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await alive.delete()
            msg = await bot.send_file(alive.chat_id, logo, caption=kecid)
            await asyncio.sleep(100)
            await msg.delete()
        except BaseException:
            await alive.edit(
                kecid + "\n\n *`Təqdim olunan logo etibarsızdır."
                "\nKeçidin logo şəklinə yönəldiyindən əmin olun`"
            )
            await asyncio.sleep(100)
            await alive.delete()
    else:
        await alive.edit(kecid)
        await asyncio.sleep(100)
        await alive.delete()            
        
        
Help = CmdHelp('salive')
Help.add_command('salive', None, 'Gif-li alive mesajı')
Help.add_info('@TheCyberUserBot üçün hazırlanmışdır.')
Help.add()                
