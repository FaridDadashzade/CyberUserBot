# Copyright (C) 2021 FaridDadashzade.
#
# Licensed under the GPL-3.0 License;
# you may not use this file except in compliance with the License.
#

# TheCyberUserBot - Faridxz

import datetime
import asyncio
import shutil
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from userbot import bot, CMD_HELP
from userbot.events import register
from asyncio.exceptions import TimeoutError
from telethon.tl.types import DocumentAttributeAudio, DocumentAttributeVideo

import os
import subprocess
from userbot.utils import progress
import glob
from random import randint
from userbot.cmdhelp import CmdHelp

# ██████ LANGUAGE CONSTANTS ██████ #

from userbot.language import get_value
LANG = get_value("song")

# ████████████████████████████████ #

@register(outgoing=True, pattern="^.deez(\d*|)(?: |$)(.*)")
async def deezl(event):
    if event.fwd_from:
        return
    sira = event.pattern_match.group(1)
    if sira == '':
        sira = 0
    else:
        sira = int(sira)

    sarki = event.pattern_match.group(2)
    if len(sarki) < 1:
        if event.is_reply:
            sarki = await event.get_reply_message().text
        else:
            await event.edit(LANG['GIVE_ME_SONG']) 

    await event.edit(LANG['SEARCHING'])
    chat = "@DeezerMusicBot"
    async with bot.conversation(chat) as conv:
        try:     
            mesaj = await conv.send_message(str(randint(31,62)))
            sarkilar = await conv.get_response()
            await mesaj.edit(sarki)
            sarkilar = await conv.get_response()
        except YouBlockedUserError:
            await event.reply(LANG['BLOCKED_DEEZER'])
            return
        await event.client.send_read_acknowledge(conv.chat_id)
        if sarkilar.audio:
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, LANG['UPLOADED_WITH'], file=sarkilar.message)
            await event.delete()
        elif sarkilar.buttons[0][0].text == "No results":
            await event.edit(LANG['NOT_FOUND'])
        else:
            await sarkilar.click(sira)
            sarki = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
            await event.client.send_read_acknowledge(conv.chat_id)
            await event.client.send_message(event.chat_id, f"`{sarkilar.buttons[sira][0].text}` | " + LANG['UPLOADED_WITH'], file=sarki.message)
            await event.delete()

@register(outgoing=True, pattern="^.song(?: |$)(.*)")
async def WooMai(netase):
    if netase.fwd_from:
        return
    song = netase.pattern_match.group(1)
    chat = "@WooMaiBot"
    link = f"/netease {song}"
    await netase.edit("```Musiqi axtarılır...```")
    async with bot.conversation(chat) as conv:
          await asyncio.sleep(2)
          await netase.edit("`Musiqi yüklənir...\n Biraz gözləyin.`")
          try:
              msg = await conv.send_message(link)
              response = await conv.get_response()
              respond = await conv.get_response()
              """ for @TheCyberUserBot """
              await bot.send_read_acknowledge(conv.chat_id)
          except YouBlockedUserError:
              await netase.reply("```Xahiş edirəm @WooMaiBot-u blokdan çıxarın.```")
              return
          await netase.edit("`Musiqi göndərilir...`")
          await asyncio.sleep(3)
          await bot.send_file(netase.chat_id, respond)
    await netase.client.delete_messages(conv.chat_id,
                                       [msg.id, response.id, respond.id])
    await netase.delete()

@register(outgoing=True, pattern="^.songpl ?(.*)")
async def songpl(event):
    if event.fwd_from:
        return
    DELAY_BETWEEN_EDITS = 0.3
    PROCESS_RUN_TIME = 100
    cmd = event.pattern_match.group(1)

    if len(cmd) < 1:
        await event.edit(LANG['USAGE_PL'])    

    reply_to_id = event.message.id
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    await event.edit(LANG['SEARCHING_PL'])
    dosya = os.getcwd() + "/playlist/" + "pl.pl"
    klasor = os.getcwd() + "/playlist/"
    sonuc = os.system(f"spotdl --playlist {cmd} --write-to=\"{dosya}\"")
    sonuc2 = os.system(f"spotdl --list {dosya} -f {klasor}")
    await event.edit(LANG['DOWNLOADED'])
    l = glob.glob(f"{klasor}/*.mp3")
    i = 0
    if len(l) >= 1:
        while i < len(l):
            await event.reply(LANG['SENDING_SONGS'] + l[i])
            await event.client.send_file(
                event.chat_id,
                l[i],
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
    else:
        await event.edit(LANG['NOT_FOUND_PL'])   
        return 
    os.system(f"rm -rf {klasor}/*.mp3")
    subprocess.check_output(f"rm -rf {klasor}/*.mp3",shell=True)
    os.system(f"rm -rf {klasor}/*.pl")
    subprocess.check_output(f"rm -rf {klasor}/*.pl",shell=True)

CmdHelp('song').add_command(
    'deez', '<şarkı ismi/youtube/spotify/soundcloud>', 'Birçok siteden şarkıyı arayıp, şarkıyı indirir.'
).add_command(
    'song', '<şarkı ismi/youtube/spotify>', 'Şarkı indirir.'
).add_command(
    'songpl', '<spotify playlist>', 'Spotify Playlist\'inden şarkı indirir'
).add()
