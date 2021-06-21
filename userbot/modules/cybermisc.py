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
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights, ChannelParticipantsKicked
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.types import MessageEntityMentionName


import logging

import asyncio
from userbot.events import register
from userbot import BOTLOG_CHATID, BOTLOG


async def get_user_from_event(event):
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit(f"**Xahiş edirəm bir istifadəçiyə cavab verin\nvə ya istifadəçi adı qeyd edin.**")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await event.edit("Xəta baş verdi! \n **XƏTA**\n", str(err))
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

try:
    from userbot import client2, client3
except BaseException:
    client2 = client3 = None


@register(outgoing=True, pattern=r"^\.gkick(?: |$)(.*)")
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.reply("`İstifadəçi bütün qruplardan atılır..`")
    else:
        rkp = await lazy.edit("`İstifadəçi bütün qruplardan atılır...`")
    me = await rk.client.get_me()
    await rkp.edit(f"**Hazırlanır...**")
    my_mention = "[{}](tg://user?id={})".format(me.first_name, me.id)
    f"@{me.username}" if me.username else my_mention
    await rk.get_chat()
    a = b = 0
    if rk.is_private:
        user = rk.chat
        reason = rk.pattern_match.group(1)
    else:
        rk.chat.title
    try:
        user, reason = await get_user_from_event(rk)
    except BaseException:
        pass
    try:
        if not reason:
            reason = 'Gizli'
    except BaseException:
        return await rkp.edit(f"**Xəta!\nNaməlum istifadəçi.**")
        testrk = [d.entity.id for d in await rk.client.get_dialogs() if (d.is_group or d.is_channel)]
        for i in testrk:
            try:
                await rk.client.edit_permissions(i, user, view_messages=False)
                await rk.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await rkp.edit(f"**İstifadəçi qrup/kanallardan atılır.\n{a} qrup/kanaldan atıldı...**")

            except BaseException:
                b += 1
    else:
        await rkp.edit(f"**Bir istifadəçiyə cavab verin.**")

    return await rkp.edit(f"**[{user.first_name}](tg://user?id={user.id}) {a} qrup/kanallardan atıldı.**")



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
	
	

@register(outgoing=True, groups_only=True, disable_errors=True, pattern=r"^\.unbanall(?: |$)(.*)")
async def _(cyber):
    await cyber.edit("`Qadağan olunmuş istifadəçiləri axtarıram...`")
    p = 0
    (await cyber.get_chat()).title
    async for i in cyber.client.iter_participants(
        cyber.chat_id,
	filter=ChannelParticipantsKicked,
        aggressive=True,
    ):
        try:
            await cyber.client.edit_permissions(cyber.chat_id, i, view_messages=True)
            p += 1
        except BaseException:
            pass
    await cyber.edit("`Qadağan olunmuş istifadəçilər siyahıdan silindi...`")	
	
	
	
Help = CmdHelp('cybermisc')
Help.add_command('undelete', None, 'Bir qrupda silinmiş 5 mesajı göndərər.')
Help.add_command('unbanall', None, 'Qrupda qadağan edilmiş bütün istifadəçilərin qadağasını silər.')
Help.add_info('@faridxz tərəfindən @TheCyberUserBot üçün hazırlanmışdır.')
Help.add() 
