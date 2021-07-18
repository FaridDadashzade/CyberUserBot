# Copyright (C) 2021
#
# CYBERUSERBOT - FARIDXZ

from userbot.cmdhelp import CmdHelp
from userbot import PLUGIN_CHANNEL_ID, CMD_HELP
from userbot.events import register
from re import search
from json import loads, JSONDecodeError
from userbot.language import LANGUAGE_JSON
from os import remove

@register(outgoing=True, pattern="^.dil ?(.*)")
@register(outgoing=True, pattern="^.lang ?(.*)")
async def dil(event):
    global LANGUAGE_JSON

    komut = event.pattern_match.group(1)
    if search(r"y[uü]kle|install", komut):
        await event.edit("`Dil faylı yüklenir...`")
        if event.is_reply:
            reply = await event.get_reply_message()
            dosya = await reply.download_media()

            if ((len(reply.file.name.split(".")) >= 2) and (not reply.file.name.split(".")[1] == "cyberjson")):
                return await event.edit("`Lütfen geçerli bir` **CYBERJSON** `dosyası verin!`")

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Lütfen geçerli bir` **CYBERJSON** `dosyası verin!`")

            await event.edit(f"`{dosya['LANGUAGE']}` `dili yükleniyor...`")
            pchannel = await event.client.get_entity(PLUGIN_CHANNEL_ID)

            dosya = await reply.download_media(file="./userbot/language/")
            dosya = loads(open(dosya, "r").read())
            await reply.forward_to(pchannel)
            
            LANGUAGE_JSON = dosya
            await event.edit(f"✅ `{dosya['LANGUAGE']}` `dili başarıyla yüklendi!`\n\n**İşlemlerin geçerli olması için botu yeniden başlatın!**")
        else:
            await event.edit("**Lütfen bir dil dosyasına yanıt verin!**")
    elif search(r"bilgi|info", komut):
        await event.edit("`Dil dosyası bilgileri getiriliyor... Lütfen bekleyiniz.`")
        if event.is_reply:
            reply = await event.get_reply_message()
            if ((len(reply.file.name.split(".")) >= 1) and (not reply.file.name.split(".")[1] == "cyberjson")):
                return await event.edit("`Lütfen geçerli bir` **CYBERJSON** `dosyası verin!`")

            dosya = await reply.download_media()

            try:
                dosya = loads(open(dosya, "r").read())
            except JSONDecodeError:
                return await event.edit("`Lütfen geçerli bir` **CYBERJSON** `dosyası verin!`")

            await event.edit(
                f"**Dil: **`{dosya['LANGUAGE']}`\n"
                f"**Dil Kodu: **`{dosya['LANGCODE']}`\n"
                f"**Tərcümə edən: **`{dosya['AUTHOR']}`\n"

                f"\n\n`Dil faylını yükləmək üçün` `.lang yükle` `yazın`"
            )
        else:
            await event.edit("**Lütfen bir dil dosyasına yanıt verin!**")
    else:
        await event.edit(
            f"**Dil: **`{LANGUAGE_JSON['LANGUAGE']}`\n"
            f"**Dil Kodu: **`{LANGUAGE_JSON['LANGCODE']}`\n"
            f"**Tərcümə edən: **`{LANGUAGE_JSON ['AUTHOR']}`\n"

            f"\n\nDiger diller üçün @CyberDil kanalına baxın"
        )

CmdHelp('dil').add_command(
    'dil', None, 'Yüklediğiniz dil hakkında bilgi verir.'
).add_command(
    'dil bilgi', None, 'Yanıt verdiğiniz dil dosyası hakkında bilgi verir.'
).add_command(
    'dil yükle', None, 'Yanıt verdiğiniz dil dosyasını yükler.'
).add()
