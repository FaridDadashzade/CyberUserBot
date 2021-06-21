# Copyright 2021 (C) FaridDadashzade.
#
# CyberUserBot - Faridxz
# 
# oğurlayan peysərdi #

import os
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from userbot import (
    HEROKU_APPNAME,
    HEROKU_APIKEY,
    SUDO_VERSION,
    SUDO_ID,
)
import heroku3
from telethon.tl.functions.users import GetFullUserRequest

Heroku = heroku3.from_key(HEROKU_APIKEY)
heroku_api = "https://api.heroku.com"
cybersudo = os.environ.get("SUDO_ID", None)


@register(outgoing=True,
          pattern=r"^.addsudo")
async def addsudo(event):
    await event.edit("[C Y B Σ R]\nİstifadəçi sudo olaraq qeyd edilir...")
    cyber = "SUDO_ID"
    if HEROKU_APPNAME is not None:
        app = Heroku.app(HEROKU_APPNAME)
    else:
        await event.edit("`[C Y B Σ R HEROKU]:" "\nXahiş edirəm` **HEROKU_APPNAME** dəyərini əlavə edin.")
        return
    heroku_var = app.config()
    if event is None:
        return
    try:
        cybert = await get_user(event)
    except Exception:
        await event.edit("Xahiş edirəm hir istifadəçiyə cavab verin.")
    if cybersudo:
        yenisudo = f"{cybersudo} {cybert}"
    else:
        yenisudo = f"{cybert}"
    await event.edit("İstifadəçi sudo olaraq qeyd edildi!\nC Y B Σ R yenidən başladılır...")
    heroku_var[cyber] = yenisudo


async def get_user(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        if previous_message.forward:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.forward.sender_id)
            )
        else:
            replied_user = await event.client(
                GetFullUserRequest(previous_message.sender_id)
            )
    cybert = replied_user.user.id
    return cybert
    
    
Help = CmdHelp('addsudo')
Help.add_command('addsudo', None, 'Cavab verdiyiniz istifadəçini botunuzda admin edər.')
Help.add_info('@Faridxz tərəfindən @TheCyberUserBot üçün hazırlanmışdır.')
Help.add()
