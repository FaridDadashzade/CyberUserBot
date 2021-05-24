from telethon import events

import asyncio
from userbot import SUDO_ID, SUDO_VERSION, CYBER_VERSION
from userbot.cmdhelp import CmdHelp
from userbot.events import register

@register(incoming=True, from_users=SUDO_ID, pattern="^.calive$")
async def sudoers(s):
    await s.client.send_message(s.chat_id,f"`C Y B Σ R USERBOT\nSudo aktivdir...\nC Y B Σ R Version: {CYBER_VERSION}\nSudo Version: {SUDO_VERSION}`")
    
Help = CmdHelp('calive')
Help.add_command('calive',   None, 'Sudo aktiv olub olmadığını yoxlamaq üçün.')
Help.add()
        