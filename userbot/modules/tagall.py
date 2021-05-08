# CYBERUSERBOT - Luciferxz #

import time
import requests

from collections import deque
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from random import choice, getrandbits, randint
from re import sub
from userbot import CMD_HELP, bot
from userbot.events import register
from userbot.modules.admin import get_user_from_event
from userbot.cmdhelp import CmdHelp

@register(outgoing=True, pattern="^.tagall$")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@tag"
    chat = await event.get_input_chat()
    leng = 0
    async for x in bot.iter_participants(chat):
        if leng < 4092:
            mentions += f"[\u2063](tg://user?id={x.id})"
            leng += 1
    await event.reply(mentions)
    await event.delete()

@register(outgoing=True, pattern="^.admin")
async def _(event):
    if event.fwd_from:
        return
    mentions = "@admin"
    chat = await event.get_input_chat()
    async for x in bot.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f"[\u2063](tg://user?id={x.id})"
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

CmdHelp('tagall').add_command(
    'tagall', None, 'Bu əmri hər hansısa söhbətdə işlədəndə hərkəsi tağ edir.'
).add_command(
    'admin', None, 'Bu əmri hər hansıxa sohbətdə işlədəndə adminləri tağ edər.'
).add()
