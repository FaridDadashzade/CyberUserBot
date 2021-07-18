# Copyright 2021 (C) FaridDadashzade
#
# CyberUserBot - Faridxz
# 
# oğurlayan peysərdi #

import requests
import re
import datetime
import logging
import bs4
import os
import asyncio
import time
import html
from telethon import *
from telethon import events
from telethon import utils
from telethon.tl import functions
from datetime import datetime
from userbot.cmdhelp import CmdHelp
from userbot import bot
from telethon.tl.types import UserStatusEmpty, UserStatusLastMonth, UserStatusLastWeek, UserStatusOffline, UserStatusOnline, UserStatusRecently, ChatBannedRights, ChannelParticipantsKicked
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.types import MessageEntityMentionName

from asyncio import sleep
from userbot.events import register
from userbot import BOTLOG_CHATID, BOTLOG, SUDO_ID


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


@register(outgoing=True, disable_errors=True, pattern=r"^\.gkick(?: |$)(.*)")
@register(incoming=True, from_users=SUDO_ID, pattern="^.cgkick$")
async def gspide(rk):
    lazy = rk
    sender = await lazy.get_sender()
    me = await lazy.client.get_me()
    if not sender.id == me.id:
        rkp = await lazy.edit("`İstifadəçi bütün qruplardan atılır..`")
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
    if user:
        if user.id == 1527722982:
            return await rkp.edit(f"`Xəta!`\n`Bunu C Y B Σ R UserBot sahibinə edə bilmərəm!`")
        try:
            await rk.client(BlockRequest(user))
            await rk.client(UnblockRequest(user))
        except BaseException:
            pass
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
		
@register(outgoing=True, pattern="^.pm ?(.*)")
async def pm(event):
 
    p = event.pattern_match.group(1)
    m = p.split(" ")

    chat_id = m[0]
    try:  
        chat_id = int(chat_id)
    except BaseException:
        
        pass
  
    msg = ""
    mssg = await event.get_reply_message() 
    if event.reply_to_msg_id:
        await event.client.send_message(chat_id, mssg)
        await event.edit("**C Y B Ξ R mesajınızı göndərdi ✔️**")
    for i in m[1:]:
        msg += i + " "
    if msg == "":
        return
    try:
        await event.client.send_message(chat_id, msg)
        await event.edit("**C Y B Ξ R mesajınızı göndərdi ✔️**")
    except BaseException:
        await event.edit("@TheCyberUserBot mesajınızı göndərə bilmədi :(")
        

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
	
	
 
@register(outgoing=True, pattern="^.sendbot (.*)")
async def sendbot(cyber):
    if cyber.fwd_from:
        return
    chat = str(cyber.pattern_match.group(1).split(' ', 1)[0])
    link = str(cyber.pattern_match.group(1).split(' ', 1)[1])
    if not link:
        return await cyber.edit("`Bağışlayın, heçnə tapa bilmədim.`")
     
    botid = await cyber.client.get_entity(chat)
    await cyber.edit("```Hazırlanır...```")
    async with bot.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=botid))
              msg = await bot.send_message(chat, link)
              response = await response
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError: 
              await cyber.reply(f"`Xahiş edirəm` {chat} `-u blokdan çıxarın və yenidən yoxlayın.`")
              return
          except :
              await cyber.edit("`Belə bir bot yoxdur :(`")
              await sleep(2)
              return await cyber.delete()
         
          await cyber.edit(f"`Göndərilən mesaj` : {link}"
                               f"\n`Kimə` : {chat}")
          await bot.send_message(cyber.chat_id, response.message)
          await bot.send_read_acknowledge(cyber.chat_id)
          """ prosesi yerine yetirdikden sonra silmesi ucun """
          await cyber.client.delete_messages(conv.chat_id,
                                                [msg.id, response.id])

		
	
Help = CmdHelp('cybermisc')
Help.add_command('undelete', None, 'Bir qrupda silinmiş 5 mesajı göndərər.')
Help.add_command('unbanall', None, 'Qrupda qadağan edilmiş bütün istifadəçilərin qadağasını silər.')
Help.add_command('sendbot', '<@botun-istifadeci-adi> <mesaj>', 'Yazdığınız əmri qeyd etdiyiniz bota göndərər və botun cavabını atar')
Help.add()


Help = CmdHelp('pm')
Help.add_command('pm', '<@istifadeci-adi> <mesaj>', 'Qeyd etdiyiniz mesajı istədiyiniz şəxsə göndərər.')
Help.add()
