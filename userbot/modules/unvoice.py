# TheCyberUserBot - Plugin: @TheMiri #
# Copyright refucion GNU/Licence @TheCyberUserBot #
# Thanks @Xacnio #

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from userbot import bot
from userbot.cmdhelp import CmdHelp
from userbot.events import register
from telethon.tl.types import DocumentAttributeAudio
import asyncio
from os import (remove, path)

@register(outgoing=True, pattern="^.ses(?: |$)(.*)")
async def seslimuzik(event):
    caption = "@TheCyberUserBot ilə səsli mesaja çevirildi."
    if event.fwd_from:
        return
    sarki = event.pattern_match.group(1)
    rep_msg = None
    if event.is_reply:
        rep_msg = await event.get_reply_message()
    if len(sarki) < 1:
        if event.is_reply:
            sarki = rep_msg.text
        else:
            await event.edit("**Mənə bir səs adı ver və ya bir səsə cavab ver!** `İstifadəsi: .ses [hərhansı bir mahnı adı]`") 
            return

    if event.is_reply:
        rep_msg = await event.get_reply_message()
        if rep_msg.audio:
            await event.edit(f"__Səs yüklənir...__")
            indir = await rep_msg.download_media()
            await event.edit(f"__Səsi yüklədim, səsli mesaj olaraq göndərirəm...__")
            voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -y -c:a libopus 'unvoice.ogg'")
            await voice.communicate()
            if path.isfile("unvoice.ogg"):
                await event.client.send_file(event.chat_id, file="unvoice.ogg", voice_note=True, caption=caption, reply_to=rep_msg)
                await event.delete()
                remove("unvoice.ogg")
            else:
                await event.edit("`Səs, səsli mesaja çevrilə bilmədi!`")
            remove(indir)
            return

    if sarki.find("{n}") != -1:
        sarki = sarki.replace("{n}", "")
        sarki = sarki.strip()
        caption = ""

    await event.edit(f"__Yazdığınız musiqi axtarılır..: {sarki}__")
    chat = "@DeezerMusicBot"
    async with bot.conversation(chat) as conv:
        try:     
            await conv.send_message(sarki)
        except YouBlockedUserError:
            await event.reply(f"`Ups deyəsən` {chat} `bloklamısan. Zəhmət olmasa bloku aç.`")
            return
        sesler = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
        await event.client.send_read_acknowledge(conv.chat_id)
        if sesler.audio:
            try:
                titlemsg = sesler.audio.attributes[0].title + " adlı səs"
            except Exception:
                titlemsg = "Ses"           
            await event.edit(f"__{titlemsg} tapıldı, yüklənir...__")
            indir = await sesler.download_media()
            await event.edit(f"__{titlemsg} adlı səsi yüklədim, səsli mesaj olaraq göndərirəm...__")
            voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -y -c:a libopus 'unvoice.ogg'")
            await voice.communicate()
            if path.isfile("unvoice.ogg"):
                await event.client.send_file(event.chat_id, file="unvoice.ogg", voice_note=True, caption=caption, reply_to=rep_msg)
                await event.delete()
                remove("unvoice.ogg")
            else:
                await event.edit("`Tapılan səs səsli mesaja çevirilə bilmədi!`")
            remove(indir)
        elif not sesler.buttons:
            await event.edit(f"`Botta uyğun şəkildə axtarmaq olmadı! Bota gedib botun cavabına baxa bilərsən. ({chat})`")             
        elif sesler.buttons[0][0].text == "Sonuç yok":
            await event.edit("`Axtardığınız mahnını tapa bilmədim! Bağışlayın.`")     
        else:
            await sesler.click(0)
            ses = await conv.wait_event(events.NewMessage(incoming=True,from_users=595898211))
            await event.client.send_read_acknowledge(conv.chat_id)
            try:
                titlemsg = ses.audio.attributes[0].title + " adlı ses"
            except Exception:
                titlemsg = "Ses"
            await event.edit(f"__{titlemsg} tapıldı, göndərilir...__")
            indir = await ses.download_media()
            await event.edit(f"__{titlemsg} `yüklədim.` **İnşAllag doğrudur :)**. `Səsli mesaj olaraq göndərirəm...`__")
            voice = await asyncio.create_subprocess_shell(f"ffmpeg -i '{indir}' -c:a libopus 'unvoice.ogg'")
            await voice.communicate()
            if path.isfile("unvoice.ogg"):
                await event.client.send_file(event.chat_id, file="unvoice.ogg", voice_note=True, caption=caption, reply_to=rep_msg)
                await event.delete()
                remove("unvoice.ogg")
            else:
                await event.edit("`Ups mahnını və ya mp3ü’ü səsli mesaja çevirə bilmədim, bir xəta baş verdi!`")

Help = CmdHelp('unvoice')
Help.add_command('ses',
    '<musiqi>',
    '@DeezerMusicBot da musiqi axtarar, taparsa səsli mesaj olaraq göndərər',
    'ses RZZA - Çək Mənim Yanımda'
    )
Help.add_command('ses',
    '<Mp3ə cavab verin>',
    'Əgər bu əmri mp3ü yanıtlayaraq etsəniz yanıtladığınız mp3ü səsli mesaj olaraq atar',
    'ses'
    )
Help.add_warning('@TheCyberUserBot')
Help.add_info('(Sonuna  {n} yazsanız səsli mesajı "@TheCyberUserBot ilə yükləndi" yazısını qaldırar.)')
Help.add()
