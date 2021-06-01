# Copyright 2021 (C) Farid Dadashzade
#
# Thanks: https://github.com/gamerfuckerofficial/CheemsBot

from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from shutil import which
from os import remove
from userbot import ALIVE_NAME, ALIVE_LOGO, bot, CYBER_VERSION
from userbot.events import register
from userbot.cmdhelp import CmdHelp

# ================= CYBER =================
DEFAULTUSER = str(ALIVE_NAME)
# ============================================


@register(outgoing=True, pattern="^.salive$")
async def salive(alive):
    """ C Y B Σ R USERBOT """
    logo = ALIVE_LOGO
    output = ("**✦ C Y B Σ R USERBOT ✦** \n"
             f"**✦ Telethon: 1.17.4** \n"
             f"**✦ Python: 3.8.6** \n"
             f"**✦ Sahibim: {DEFAULTUSER}** \n"
             f"**✦ C Y B Σ R Version: {CYBER_VERSION}** \n"
             f"**✦ Branch: Master**")
    if ALIVE_LOGO:
        try:
            logo = ALIVE_LOGO
            await bot.send_file(alive.chat_id, logo, caption=output)
            await alive.delete()
        except BaseException:
            await alive.edit(output + "\n\n `Qeyd edilən logo yanlışdır."
                             "\nXahiş edirəm düzgün bir link qeyd edin.`")
    else:
        await alive.edit(output)            
        
        
Help = CmdHelp('salive')
Help.add_command('salive', None, 'Gif-li alive mesajı')
Help.add_info('@TheCyberUserBot üçün hazırlanmışdır.')
Help.add()                
