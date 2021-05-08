# CYBERUSERBOT - Luciferxz

from userbot.events import register
from userbot import CMD_HELP
from userbot import LYDIA_API_KEY
import coffeehouse as cf
from coffeehouse.lydia import LydiaAI
from coffeehouse.api import API
import asyncio
import logging
from userbot.cmdhelp import CmdHelp

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("lydia")

# ████████████████████████████████ #

try:
    from userbot.modules.sql_helper.lydia_sql import get_s, get_all_s, add_s, remove_s
except:
    logging.log(level=logging.WARNING,
                msg="Lydia veritabanı linki uğursuz oldu")

# SQL dışı mod
ACC_LYDIA = {}

if LYDIA_API_KEY:
    api_key = LYDIA_API_KEY
    api_client = API(api_key)
    lydia = LydiaAI(api_client)


@register(outgoing=True, pattern="^.repcf$")
async def repcf(event):
    if event.fwd_from:
        return
    await event.edit(LANG['WORKING'])
    try:
        session = lydia.create_session()
        reply = await event.get_reply_message()
        msg = reply.text
        text_rep = session.think_thought(msg)
        await event.edit(LANG['LYDIA_SAYS'].format(text_rep))
    except Exception as e:
        await event.edit(str(e))

@register(outgoing=True, pattern="^.addcf$")
async def addcf(event):
    if event.fwd_from:
        return
    await event.edit(LANG['SQL_OFF'])
    await asyncio.sleep(3)
    await event.edit(LANG['WORKING'])
    reply_msg = await event.get_reply_message()
    if reply_msg:
        session = lydia.create_session()
        session_id = session.id
        if reply_msg.from_id is None:
            return await event.edit(LANG['REPLY_USER_ERR'])
        ACC_LYDIA.update({(event.chat_id & reply_msg.from_id): session})
        await event.edit(LANG['LYDIA_ACTIVATED'].format(str(reply_msg.from_id), str(event.chat_id)))
    else:
        await event.edit(LANG['REPLY_FOR_ACTIVATE'])

@register(outgoing=True, pattern="^.remcf$")
async def remcf(event):
    if event.fwd_from:
        return
    await event.edit(LANG['SQL_OFF'])
    await asyncio.sleep(3)
    await event.edit("İşlənir...")
    reply_msg = await event.get_reply_message()
    try:
        del ACC_LYDIA[event.chat_id & reply_msg.from_id]
        await event.edit(LANG['LYDIA_DEACTIVATED'].format(str(reply_msg.from_id), str(event.chat_id)))
    except Exception:
        await event.edit(LANG['LYDIA_OFF_FOR_USER'])


@register(incoming=True, disable_edited=True)
async def user(event):
    user_text = event.text
    try:
        session = ACC_LYDIA[event.chat_id & event.from_id]
        msg = event.text
        async with event.client.action(event.chat_id, "typing"):
            text_rep = session.think_thought(msg)
            wait_time = 0
            for i in range(len(text_rep)):
                wait_time = wait_time + 0.1
            await asyncio.sleep(wait_time)
            await event.reply(text_rep)
    except (KeyError, TypeError):
        return

CmdHelp('lydia').add_command(
    'addcf', '<istifadəçi adı/cavablayaraq>', 'Lydia\'nın avtomatik söhbətini aktivləşdirir.'
).add_command(
    'remcf', '<istifadəçi adı/cavablayaraq>', 'Lydia\'nın avtomatik söhbətini deaktivləşdirir.'
).add_command(
    'repcf', '<istifadəçi adı/cavablayaraq>', 'Lydia\'nın avtomatik söhbətini xüsusi istifadəçi üçün aktivləşdirir.'
).add()
