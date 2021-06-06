# Copyright 2021 (C) FaridDadashzade
#
# CyberUserBot - Faridxz
# 
# oğurlayan peysərdi #

import requests
import bs4
import os
import asyncio
import time
import html
from telethon import *
from telethon import events
from telethon.tl import functions
from datetime import datetime
from userbot.cmdhelp import CmdHelp
from userbot import bot
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName


import logging

import asyncio
from userbot.events import register
from userbot import BOTLOG_CHATID, BOTLOG


@register(outgoing=True, disable_errors=True, incoming=True, func=lambda e: e.mentioned)
async def ltgm(event):
    hmm = await event.get_chat()
        
    if BOTLOG_CHATID:
        sender = await event.get_sender()
        await asyncio.sleep(5)
        if not event.is_private and not (await event.get_sender()).bot:
            await event.client.send_message(
                BOTLOG_CHATID,
                f"#TAG \n<b>Mesajı göndərən : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
			\n<b>Qrup : </b><code>{hmm.title}</code>\
                        \n<b>Mesaj : </b><a href = 'https://t.me/c/{hmm.id}/{event.message.id}'> link</a>",
                parse_mode="html",
                link_preview=True,
            )
            e = await event.client.get_entity(int(BOTLOG_CHATID))
            fwd_message = await event.client.forward_messages(
                    e,
                    event.message,
                    silent=True
                )
        else:
            if event.is_private:
                if not (await event.get_chat()).bot:
                    await event.client.send_message(
                        BOTLOG_CHATID,
                        f"#TAG \n<b>Mesajı göndərən : </b><a href = 'tg://user?id={sender.id}'> {sender.first_name}</a>\
                                \n<b>ID : </b><code>{sender.id}</code>",
                        parse_mode="html",
                        link_preview=True,
                    )
                    e = await event.client.get_entity(int(BOTLOG_CHATID))
                    fwd_message = await event.client.forward_messages(
                            e,
                            event.message,
                            silent=True
                        )
		


@register(outgoing=True, pattern="^.undelete(?: |$)(.*)")
async def undelete(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await bot.get_admin_log(event.chat_id, limit=5, search="", edit=False, delete=True)
        for i in a:
            await event.reply(i.original.action.message)
    else:
        await event.edit("Bu əmri yerinə yetirmək üçün admin olmalısınız!")
        await asyncio.sleep(3)
        await event.delete()		

	
Help = CmdHelp('undelete')
Help.add_command('undelete', None, 'Bir qrupda silinmiş 5 mesajı göndərər')
Help.add_info('@faridxz tərəfindən @TheCyberUserBot üçün hazırlanmışdır.')
Help.add()  

