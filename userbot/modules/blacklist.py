# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#

# TheCyberUserBot - Luciferxz

import io
import re

import userbot.modules.sql_helper.blacklist_sql as sql
from userbot import CMD_HELP
from userbot.events import register
from requests import get
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("blacklist")

# ████████████████████████████████ #

KUFURLER = get('https://gitlab.com/whomiri/spacehelper/-/raw/master/forbidden.json').json()
@register(incoming=True, disable_edited=True, disable_errors=True)
async def on_new_message(event):
    name = event.raw_text
    snips = sql.get_chat_blacklist(event.chat_id)
    for snip in snips:
        if snip == "küfür":
            for kufur in KUFURLER:
                pattern = r"( |^|[^\w])" + re.escape(kufur) + r"( |$|[^\w])"
                if re.search(pattern, name, flags=re.IGNORECASE):
                    try:
                        await event.delete()
                    except:
                        await event.reply(LANG['FORBIDDEN_KUFUR'])
                        sql.rm_from_blacklist(event.chat_id, "kufur")
                    break
                pass
            continue
        else:
            pattern = r"( |^|[^\w])" + re.escape(snip) + r"( |$|[^\w])"
            if re.search(pattern, name, flags=re.IGNORECASE):
                try:
                    await event.delete()
                except Exception as e:
                    await event.reply(LANG['HAVENT_PERMISSION'])
                    sql.rm_from_blacklist(event.chat_id, snip.lower())
                break
            pass



@register(outgoing=True, pattern="^.küfür ?(.*)")
@register(outgoing=True, pattern="^.otoblist ?(.*)")
@register(outgoing=True, pattern="^.s[oö]y[üu]ş ?(.*)")
async def kufur(event):
    kufur = event.pattern_match.group(1)
    if len(kufur) < 1:
        await event.edit(LANG['USAGE_KUFUR'])
    
    if kufur == "aç":
        sql.add_to_blacklist(event.chat_id, "küfür")
        await event.edit(LANG['OPENED_KUFUR'])
    elif kufur == "bağla":
        if sql.rm_from_blacklist(event.chat_id, "küfür"):
            await event.edit(LANG['CLOSED_KUFUR'])
        else:
            await event.edit(LANG['ALREADY_CLOSED_KUFUR'])


@register(outgoing=True, pattern="^.addblacklist(?: |$)(.*)")
async def on_add_black_list(addbl):
    if addbl.is_reply:
        reply = await addbl.get_reply_message()
        text = reply.text
    else:
        text = addbl.pattern_match.group(1)
    to_blacklist = text.split()
    for trigger in to_blacklist:
        sql.add_to_blacklist(addbl.chat_id, trigger)
    await addbl.edit("{} **{}**".format(len(to_blacklist), LANG['ADDED']))

@register(outgoing=True, pattern="^.listblacklist(?: |$)(.*)")
async def on_view_blacklist(listbl):
    all_blacklisted = sql.get_chat_blacklist(listbl.chat_id)
    OUT_STR = f"**{LANG['BLACKLIST']}**\n"
    if len(all_blacklisted) > 0:
        for trigger in all_blacklisted:
            OUT_STR += f"`{trigger}`\n"
    else:
        OUT_STR = LANG['NOT_FOUND']
    if len(OUT_STR) > 4096:
        with io.BytesIO(str.encode(OUT_STR)) as out_file:
            out_file.name = "blacklist.text"
            await listbl.client.send_file(
                listbl.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=LANG['BLACKLIST_FILE'],
                reply_to=listbl
            )
            await listbl.delete()
    else:
        await listbl.edit(OUT_STR)

@register(outgoing=True, pattern="^.rmblacklist(?: |$)(.*)")
async def on_delete_blacklist(rmbl):
    text = rmbl.pattern_match.group(1)
    to_unblacklist = list(set(trigger.strip() for trigger in text.split("\n") if trigger.strip()))
    successful = 0
    for trigger in to_unblacklist:
        if sql.rm_from_blacklist(rmbl.chat_id, trigger.lower()):
            successful += 1
    await rmbl.edit(LANG['REMOVED'])
    
CmdHelp('blacklist').add_command(
    'listblacklist', None, 'Bir sohbetteki aktiv blacklisti göstərər.'
).add_command(
    'addblacklist', '<kəlimə(lər)/cavap>', 'Mesajı \'qara list bölməsinə\' qeydedər. \'Kara liste anahtar kelimesinden\' bahsedildiğinde bot iletiyi siler.', '.addblacklist amk'
).add_command(
    'rmblacklist', '<kelime>', 'Belirtilen kara listeyi durdurur.', '.rmblacklist amk'
).add_command(
    'otoblist', '<aç/bağla>', 'Oto Blacklisti açar grupda söyüş söyən olsa silər', '.otoblist aç'
).add_warning('Bu işlemleri gerçekleştirmek için yönetici olmalı ve **Mesaj Silme** yetkiniz olmalı.').add()
